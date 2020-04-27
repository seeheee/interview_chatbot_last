from django.shortcuts import render, get_object_or_404, reverse, redirect
from .forms import ResumeForm
from resume.models import Resume, MBTI, All
from user.models import User
from bot.models import QuestionList, TestQuestionList

def homePage(request):
    form = ResumeForm()
    return render(request, 'home/index.html', {'form': form})

def details(request):
    form = ResumeForm()
    return render(request, 'home/details.html', {'form': form})
#내가 하려던게 resume.pk값을 user DB에 있는 my_resume에 넣어주려던거라 form이 사용자 form일듯?

def mypage(request):
    user = request.user
    if user.my_resume == 0:
        mbtis = MBTI.objects.all()
        return render(request, 'mbti_test.html', {'mbtis': mbtis})
    else:
        if request.method == "POST":
            item_id = request.POST.get('item_id')
            my_resume = get_object_or_404(Resume, pk=item_id)
            user = request.user
            user.my_resume = my_resume.id
            print(user.my_resume)
            user.save()
            mbtis = MBTI.objects.filter(my_resume=item_id).order_by('-id')
            resumes = Resume.objects.filter(author=user).order_by('-id')

            return render(request, 'home/mypage.html',
                          {'my_resume': my_resume, 'resumes': resumes, 'user': user, 'mbtis': mbtis})
        else:
            user = request.user
            mbtis = MBTI.objects.filter(my_resume=user.my_resume).order_by('-id')
            my_resume = get_object_or_404(Resume, pk=user.my_resume)
            resumes = Resume.objects.filter(author=user).order_by('-id')

    return render(request, 'home/mypage.html', {'my_resume': my_resume, 'resumes': resumes, 'user':user, 'mbtis':mbtis})

def result_list(request):
    user = request.user
    resumes = Resume.objects.filter(author=user).order_by('-id')
    questions = QuestionList.objects.all().order_by('-id')[:1]
    test = TestQuestionList.objects.all().order_by('-id')[:1]
    word_list = QuestionList.objects.all().order_by('-id')[:1].values('word_count')
    word_list = str(word_list)[28:-5].strip(" ").replace(" ", "").replace("'", "").replace("tag:", "").replace("count:", "").replace("},{", " ").replace(",",":").replace("{", "").replace("}", "")
    word_list = word_list.split(" ")
    word_dict = {}
    for word in word_list:
        word = word.split(":")
        word_dict[word[0]] = word[1]
    print(word_dict)

    word_list2 = All.objects.all().order_by('-id')[:1].values('word_count')
    word_list2 = str(word_list2)[28:-5].strip(" ").replace(" ", "").replace("'", "").replace("tag:", "").replace("count:", "").replace("},{", " ").replace(",", ":").replace("{", "").replace("}", "")
    word_list2 = word_list2.split(" ")
    word_dicts = {}
    for words in word_list2:
        words = words.split(":")
        word_dicts[words[0]] = words[1]
    print(word_dicts)

    return render(request, 'home/result_list.html', {'resumes': resumes, 'questions': questions, 'test': test, 'word_dict': word_dict, 'word_dicts': word_dicts})

def contact(request):
    form = ResumeForm()
    return render(request, 'home/contact.html', {'form': form})
