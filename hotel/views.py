from django.shortcuts import render, get_object_or_404,redirect
#from django.views.generic.detail import DetailView
from django.views.generic import ListView,TemplateView
from .models import hotel
from django.contrib.auth.models import User, auth
from reviews.models import review
from complaint.models import complaint
from question.models import question
from mobileusers.models import mobileuser
from graph.views import get_total_score_doughnut, get_question_pie
import ast


def hotel_list_view(request,id):
    hotel_detail = hotel.objects.all()
    hotelspecific = id
    marker = get_marker(id)

    # graph for overall score
    overall_script, overall_div = get_total_score_doughnut(id)

    # graphs for each questions
    questions_script, questions_div = get_question_answer_graph(id)

    total_script = overall_script + questions_script
    
    context = {
        'id': hotelspecific,
        'hotel_detail': hotel_detail,
        'marker' : marker,
        'overall_div' : overall_div,
        'questions_div': questions_div,
        'total_script' :total_script
        # 'overall_script' : overall_script,
        # 'q_div': q_div,
    }

    return render(request,'hotelview.html',context)

def get_marker(hotel_id):
    """
        This function will return the list of markers for all hotels in review table
    """
    marker = []
    latlng = ast.literal_eval(hotel.objects.filter(id = hotel_id).values('geo_tag')[0]['geo_tag'])
    marker.append(latlng['longitude'])
    marker.append(latlng['latitude'])
        
    return marker


def get_question_answer_graph(hotel_id):
    """
    this function will get a hotel_id as an input and return pie graphs for all
    questions and answers
    """
    questions_temp = [
        "How Often Do You Dine with Us?",
        "How good was the outside environment of the restaurant?",
        "What Did You Like Best About Our Food and Services?",
        "How Quick or Adequate Was the Speed of Service?"
    ]

    questions_script = ''
    questions_div = ''
    for q in questions_temp:
        q_script, q_div = get_question_pie(hotel_id, q)
        questions_script = questions_script + q_script
        questions_div = questions_div + q_div

    return [questions_script, questions_div]