from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse
from django.template import loader

from app.models import JobPost

job_title = [
    "First Job",
    "Second Job",
    "Third Job"
]

job_description = [
    "First job description",
    "Second job description",
    "Third job description"
]



# Create your views here.
# def hello(request):
#     return HttpResponse("<h3>Hello World</h3>")

class TempClass:
    x = 5

def hello(request):
    list = ["alpha", "beta"]
    temp = TempClass()
    is_authenticated = False
    context={"name":"Django", "age":30, "first_list":list, "temp_object":temp,
            "is_authenticated":is_authenticated}
    return render(request, "app/hello.html",context)

def job_list(request):
    # <ul><li>Job 1</li> <li>Job 2</li> <li>Job 3</li></ul>
    # list_of_jobs = "<ul>"
    # for j in job_title:
    #     job_id = job_title.index(j)
    #     detail_url = reverse('jobs_detail', args=(job_id,))
    #     list_of_jobs += f"<li><a href='{detail_url}'>{j}</a></li>"
    # list_of_jobs += "</ul>"
    # return HttpResponse(list_of_jobs)
    # job_post = JobPost.objects.values_list('title',flat=True)
    job_post = JobPost.objects.all()
    print("job_title------------------->",job_title)
    # context={"job_title_list":job_title}
    context={"jobs":job_post}
    return render(request, "app/index.html", context)


def job_detail(request, slug):
    try:
        if id == 0:
            return redirect(reverse('jobs_home'))
        # return_html = f"<h1>{job_title[id]}</h1> <h3>{job_description[id]}</h3>"
        # return HttpResponse(return_html)
        job_post = JobPost.objects.get(slug=slug)
        # context={"job_title":job_post.title, "job_description":job_post.description,"salary":job_post.salary}
        return render(request, "app/job_detail.html", context={'job':job_post})
    except:
        return HttpResponseNotFound("Not Found")