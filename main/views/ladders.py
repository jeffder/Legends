# Ladder views

from django.contrib.auth.decorators import login_required
from django.db.models.loading import get_model
from django.shortcuts import redirect, render_to_response, render
from django.template import RequestContext

from main.models import (
    Club, Round, LegendsLadder, ColemanLadder, CrowdsLadder,
    MarginsLadder, BrownlowLadder, AFLLadder, StreakLadder
)
from main.views.auth import render_auth_form
from main.views.tips_and_results import render_in_progress

selected_page = 'ladders'


@login_required
def view_ladder(request, round_id=None, view_name=None):
    """
    Show:
        * the ladder for the latest completed round if round_id isn't specified
          or final.
        * the ladder for the last home/away round if round is a finals round.
        * the Legends ladder if view_name isn't specified.
    """
    live_round = Round.objects.get(id=request.session['live_round'])
    if round_id:
        selected_round = Round.objects.get(id=round_id)
    else:
        selected_round = live_round

    if selected_round.is_finals:
        selected_round = Round.objects   \
            .filter(season=selected_round.season)   \
            .filter(is_finals=False)   \
            .reverse()[0]

        if view_name:
            redirect_url = '/legends/%s/%s/' % (selected_round.id, view_name)
        else:
            redirect_url = '/legends/%s/ladders/' % selected_round.id

        return redirect(redirect_url)

    if not selected_round.status in ('Provisional', 'Final'):
        # There won't be a ladder if no games have been played for the season,
        # so redirect to the tips page for Round 1 (eventually)
        if selected_round.name == 'Round 1':
            redirect_url = '/legends/%s/tips/' % selected_round.id

        else:
            selected_round = selected_round.previous_round

            if view_name:
                redirect_url = '/legends/%s/%s/' % (selected_round.id, view_name)
            else:
                redirect_url = '/legends/%s/ladders/' % selected_round.id

        return redirect(redirect_url)

    if not view_name:
        view_name = 'view_legends_ladder'
    ladder_name = view_name.split('_')[1]

    content = render_ladder_nav(request, selected_round, ladder_name)

    # Render the in progress banner
#    in_progress_content = render_in_progress(request, curr_round)
#    if in_progress_content:
#        content += in_progress_content

    content += render_ladder(request, ladder_name, selected_round)

    # Render the projected ladder
#    if not curr_round.is_finals and ladder_name == 'legends':
#        content += render_projected_ladder(request, curr_round)

    auth_form = render_auth_form(request)

    content += auth_form

    context = {
        'content': content,
        'club': Club.objects.get(id=request.session['club']),
        'live_round': live_round,
        'selected_page': selected_page
    }

    return render_to_response(
        'main.html',
        context,
        context_instance=RequestContext(request)
    )


def render_ladder(request, ladder_name, selected_round):
    """
    Render a ladder given the round and ladder name.
    """

    model = get_model('main', '%sLadder' % ladder_name.title())

    template = 'view_%s_ladder.html' % ladder_name

    # The streaks ladder is different from all the rest, so...
    if ladder_name == 'streak':
        unsorted = model.objects.filter(round=selected_round)
        ladder = sort_streaks_ladder(unsorted)
    else:
        ladder = model.objects.filter(round=selected_round).order_by('position')

    content = render_to_response(
        template,
        {
            'selected_round': selected_round,
            'ladder': ladder
        },
        context_instance=RequestContext(request)
    )

    return content.content


def render_projected_ladder(request, curr_round):
    '''
    Render the projected Legends ladder for given the round.
    '''

    def _sort_keys(row):
        return (-row.points, -row.percentage, -row.score_for, row.club)

    # We probably don't need to do this but let's play safe...
    rows = sorted(FinalLadder.objects.filter(round=curr_round), key=_sort_keys)

    content = render_to_response(
        'view_projected_ladder.html',
        {
            'curr_round': curr_round,
            'ladder_rows': rows
        },
        context_instance=RequestContext(request)
    )

    return content.content


def render_ladder_nav(request, selected_round, ladder_name):
    """
    Render the ladder navigation buttons.
    """

    rounds = Round.objects.filter(
        season=selected_round.season,
        is_finals=False,
        status__in=('Provisional', 'Final')
    ).order_by('start_time')

    ladder_names = (
        'Legends', 'Coleman', 'Brownlow', 'Margins',
        'Crowds', 'Form Guide', 'AFL'
    )

    if ladder_name.lower() == 'afl':
        ladder_name = 'AFL'
    elif ladder_name == 'streak':
        ladder_name = 'Form Guide'
    else:
        ladder_name = ladder_name.title()

    ladder_nav = render(
        request,
        'ladder_nav.html',
        {
            'selected_round': selected_round,
            'rounds': rounds,
            'ladder_name': ladder_name,
            'ladder_names': ladder_names
        }
    )

    return ladder_nav.content


def sort_streaks_ladder(ladders):
    """
    Sort a streaks ladder by number of latest wins, draws and losses ignoring
    byes. Use club as a tiebreaker.
    """

    def key(ladder):
        key = ladder.streak.replace('W', '0')
        key = key.replace('D', '1')
        key = key.replace('L', '2')
        key = key.replace('B', '')

        return int(key[::-1])

    unsorted = list(ladders.order_by('club'))
    return sorted(unsorted, key=key)