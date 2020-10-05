from django.http import HttpResponse
from django.shortcuts import render,redirect
from pymongo import MongoClient
import nltk.classify.util
from pymongo import MongoClient
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from django.contrib.auth.models import User,auth
from django.contrib import messages

democlient = MongoClient()
myclient=MongoClient('localhost',27017)
mydb=myclient["minordb"]

def index(request):
    return render(request,'index.html')

def shop(request):
    return render(request,'shop.html')
def poco(request):
    return render(request,'poco.html')
def analyze(request):
    mycoll=mydb["poco"]
    def extract_features(word_list):
        return dict([(word, True) for word in word_list])

    #if __name__ == "__main__":\\
    global positive_fileids,negative_fileids
    positive_fileids = movie_reviews.fileids("pos")
    negative_fileids = movie_reviews.fileids("neg")
    features_positive = [
        (extract_features(movie_reviews.words(fileids=[f])), "Positive")
        for f in positive_fileids
    ]
    features_negative = [
        (extract_features(movie_reviews.words(fileids=[f])), "Negative")
        for f in negative_fileids
    ]
    # Split the data into train and test (80/20)
    threshold_factor = 1.0
    threshold_positive = int(threshold_factor * len(features_positive))
    threshold_negative = int(threshold_factor * len(features_negative))
    features_train = (
        features_positive[:threshold_positive] + features_negative[:threshold_negative]
    )
    features_test = (
        features_positive[threshold_positive:] + features_negative[threshold_negative:]
    )
    #print("\nNumber of training datapoints:", len(features_train))
    #print("Number of test datapoints:", len(features_test))
    # Train a Naive Bayes classifier
    classifier = NaiveBayesClassifier.train(features_train)


    djtext = request.GET.get('text', 'default')
    analyzed=djtext
    mylist={}
    key1=("Reviews")
    passkey1=key1
    key2=("Ratings")
    passkey2=key2
    
    input_reviews = [analyzed]
    mylist.update({passkey1:analyzed})
    #print(mylist)
    #print("\nPredictions:")
    for review in input_reviews:
        print("\nReview:", review)
        probdist = classifier.prob_classify(extract_features(review.split()))
        pred_sentiment = probdist.max()
    #print("Predicted sentiment:", pred_sentiment)
    #print("Probability:", round(probdist.prob(pred_sentiment), 2))
    if  pred_sentiment=="Positive":
        if round(probdist.prob(pred_sentiment), 2)>=0.80:
            #print("Ratings calculated")
            rating=5.0
            mylist.update({passkey2:rating})
            
        elif round(probdist.prob(pred_sentiment), 2)>0.70 and round(probdist.prob(pred_sentiment), 2)<0.80:
            #print("Ratings calculated")
            rating=4.0
            mylist.update({passkey2:rating})
           
        elif round(probdist.prob(pred_sentiment), 2)>0.60 and round(probdist.prob(pred_sentiment), 2)<0.50:
            #print("Ratings calculated")
            rating=3.0
            mylist.update({passkey2:rating})
            
    elif pred_sentiment=="Negative":
        if round(probdist.prob(pred_sentiment), 2)>=0.80:
            #print("Ratings calculated")
            rating=1.0
            mylist.update({passkey2:rating})
            #print("*")
        elif round(probdist.prob(pred_sentiment), 2)<0.80:
            #print("Ratings calculated")
            rating=2.0
            mylist.update({passkey2:rating})
           # print("**")
    x=mycoll.insert_one(mylist)
    y=mycoll.aggregate([{"$group":{"_id":"null", "avgrating":{"$avg":"$Ratings"}}}])
    result=list(y)
    dekh={'id':result[0]['avgrating']}
    

    #return render(request,'check.html',dekh)

    params = {'mypred':pred_sentiment,'myreviews':analyzed,'myrating':mylist['Ratings'],'id':result[0]['avgrating']}
    return render(request,'analyze.html',params)
def realme(request):
    return render(request,'realme.html')
def analyze2(request):
    mycoll=mydb["realme"]
    def extract_features(word_list):
        return dict([(word, True) for word in word_list])

    #if __name__ == "__main__":\\
    global positive_fileids,negative_fileids
    positive_fileids = movie_reviews.fileids("pos")
    negative_fileids = movie_reviews.fileids("neg")
    features_positive = [
        (extract_features(movie_reviews.words(fileids=[f])), "Positive")
        for f in positive_fileids
    ]
    features_negative = [
        (extract_features(movie_reviews.words(fileids=[f])), "Negative")
        for f in negative_fileids
    ]
    # Split the data into train and test (80/20)
    threshold_factor = 1.0
    threshold_positive = int(threshold_factor * len(features_positive))
    threshold_negative = int(threshold_factor * len(features_negative))
    features_train = (
        features_positive[:threshold_positive] + features_negative[:threshold_negative]
    )
    features_test = (
        features_positive[threshold_positive:] + features_negative[threshold_negative:]
    )
    #print("\nNumber of training datapoints:", len(features_train))
    #print("Number of test datapoints:", len(features_test))
    # Train a Naive Bayes classifier
    classifier = NaiveBayesClassifier.train(features_train)


    djtext = request.GET.get('text', 'default')
    analyzed=djtext
    mylist={}
    key1=("Reviews")
    passkey1=key1
    key2=("Ratings")
    passkey2=key2
    
    input_reviews = [analyzed]
    mylist.update({passkey1:analyzed})
    #print(mylist)
    #print("\nPredictions:")
    for review in input_reviews:
        print("\nReview:", review)
        probdist = classifier.prob_classify(extract_features(review.split()))
        pred_sentiment = probdist.max()
    #print("Predicted sentiment:", pred_sentiment)
    #print("Probability:", round(probdist.prob(pred_sentiment), 2))
    if  pred_sentiment=="Positive":
        if round(probdist.prob(pred_sentiment), 2)>=0.80:
            #print("Ratings calculated")
            rating=5.0
            mylist.update({passkey2:rating})
            
        elif round(probdist.prob(pred_sentiment), 2)>0.70 and round(probdist.prob(pred_sentiment), 2)<0.80:
            #print("Ratings calculated")
            rating=4.0
            mylist.update({passkey2:rating})
           
        elif round(probdist.prob(pred_sentiment), 2)>0.60 and round(probdist.prob(pred_sentiment), 2)<0.50:
            #print("Ratings calculated")
            rating=3.0
            mylist.update({passkey2:rating})
            
    elif pred_sentiment=="Negative":
        if round(probdist.prob(pred_sentiment), 2)>=0.80:
            #print("Ratings calculated")
            rating=1.0
            mylist.update({passkey2:rating})
            #print("*")
        elif round(probdist.prob(pred_sentiment), 2)<0.80:
            #print("Ratings calculated")
            rating=2.0
            mylist.update({passkey2:rating})
           # print("**")
    x=mycoll.insert_one(mylist)
    y=mycoll.aggregate([{"$group":{"_id":"null", "avgrating":{"$avg":"$Ratings"}}}])
    result=list(y)
    dekh={'id':result[0]['avgrating']}
    

    

    params = {'mypred':pred_sentiment,'myreviews':analyzed,'myrating':mylist['Ratings'],'id':result[0]['avgrating']}
    return render(request,'analyze2.html',params)
def moto(request):
    return render(request,'moto.html')
def analyze3(request):
    mycoll=mydb["moto"]
    def extract_features(word_list):
        return dict([(word, True) for word in word_list])

    #if __name__ == "__main__":\\
    global positive_fileids,negative_fileids
    positive_fileids = movie_reviews.fileids("pos")
    negative_fileids = movie_reviews.fileids("neg")
    features_positive = [
        (extract_features(movie_reviews.words(fileids=[f])), "Positive")
        for f in positive_fileids
    ]
    features_negative = [
        (extract_features(movie_reviews.words(fileids=[f])), "Negative")
        for f in negative_fileids
    ]
    # Split the data into train and test (80/20)
    threshold_factor = 1.0
    threshold_positive = int(threshold_factor * len(features_positive))
    threshold_negative = int(threshold_factor * len(features_negative))
    features_train = (
        features_positive[:threshold_positive] + features_negative[:threshold_negative]
    )
    features_test = (
        features_positive[threshold_positive:] + features_negative[threshold_negative:]
    )
    #print("\nNumber of training datapoints:", len(features_train))
    #print("Number of test datapoints:", len(features_test))
    # Train a Naive Bayes classifier
    classifier = NaiveBayesClassifier.train(features_train)


    djtext = request.GET.get('text', 'default')
    analyzed=djtext
    mylist={}
    key1=("Reviews")
    passkey1=key1
    key2=("Ratings")
    passkey2=key2
    
    input_reviews = [analyzed]
    mylist.update({passkey1:analyzed})
    #print(mylist)
    #print("\nPredictions:")
    for review in input_reviews:
        print("\nReview:", review)
        probdist = classifier.prob_classify(extract_features(review.split()))
        pred_sentiment = probdist.max()
    #print("Predicted sentiment:", pred_sentiment)
    #print("Probability:", round(probdist.prob(pred_sentiment), 2))
    if  pred_sentiment=="Positive":
        if round(probdist.prob(pred_sentiment), 2)>=0.80:
            #print("Ratings calculated")
            rating=5.0
            mylist.update({passkey2:rating})
            
        elif round(probdist.prob(pred_sentiment), 2)>0.70 and round(probdist.prob(pred_sentiment), 2)<0.80:
            #print("Ratings calculated")
            rating=4.0
            mylist.update({passkey2:rating})
           
        elif round(probdist.prob(pred_sentiment), 2)>0.60 and round(probdist.prob(pred_sentiment), 2)<0.50:
            #print("Ratings calculated")
            rating=3.0
            mylist.update({passkey2:rating})
            
    elif pred_sentiment=="Negative":
        if round(probdist.prob(pred_sentiment), 2)>=0.80:
            #print("Ratings calculated")
            rating=1.0
            mylist.update({passkey2:rating})
            #print("*")
        elif round(probdist.prob(pred_sentiment), 2)<0.80:
            #print("Ratings calculated")
            rating=2.0
            mylist.update({passkey2:rating})
           # print("**")
    x=mycoll.insert_one(mylist)
    y=mycoll.aggregate([{"$group":{"_id":"null", "avgrating":{"$avg":"$Ratings"}}}])
    result=list(y)
    dekh={'id':result[0]['avgrating']}
    

    

    params = {'mypred':pred_sentiment,'myreviews':analyzed,'myrating':mylist['Ratings'],'id':result[0]['avgrating']}
    return render(request,'analyze3.html',params)
def rog(request):
    return render(request,'rog.html')
def analyze4(request):
    mycoll=mydb["rog"]
    def extract_features(word_list):
        return dict([(word, True) for word in word_list])

    #if __name__ == "__main__":\\
    global positive_fileids,negative_fileids
    positive_fileids = movie_reviews.fileids("pos")
    negative_fileids = movie_reviews.fileids("neg")
    features_positive = [
        (extract_features(movie_reviews.words(fileids=[f])), "Positive")
        for f in positive_fileids
    ]
    features_negative = [
        (extract_features(movie_reviews.words(fileids=[f])), "Negative")
        for f in negative_fileids
    ]
    # Split the data into train and test (80/20)
    threshold_factor = 1.0
    threshold_positive = int(threshold_factor * len(features_positive))
    threshold_negative = int(threshold_factor * len(features_negative))
    features_train = (
        features_positive[:threshold_positive] + features_negative[:threshold_negative]
    )
    features_test = (
        features_positive[threshold_positive:] + features_negative[threshold_negative:]
    )
    #print("\nNumber of training datapoints:", len(features_train))
    #print("Number of test datapoints:", len(features_test))
    # Train a Naive Bayes classifier
    classifier = NaiveBayesClassifier.train(features_train)


    djtext = request.GET.get('text', 'default')
    analyzed=djtext
    mylist={}
    key1=("Reviews")
    passkey1=key1
    key2=("Ratings")
    passkey2=key2
    
    input_reviews = [analyzed]
    mylist.update({passkey1:analyzed})
    #print(mylist)
    #print("\nPredictions:")
    for review in input_reviews:
        print("\nReview:", review)
        probdist = classifier.prob_classify(extract_features(review.split()))
        pred_sentiment = probdist.max()
    #print("Predicted sentiment:", pred_sentiment)
    #print("Probability:", round(probdist.prob(pred_sentiment), 2))
    if  pred_sentiment=="Positive":
        if round(probdist.prob(pred_sentiment), 2)>=0.80:
            #print("Ratings calculated")
            rating=5.0
            mylist.update({passkey2:rating})
            
        elif round(probdist.prob(pred_sentiment), 2)>0.70 and round(probdist.prob(pred_sentiment), 2)<0.80:
            #print("Ratings calculated")
            rating=4.0
            mylist.update({passkey2:rating})
           
        elif round(probdist.prob(pred_sentiment), 2)>0.60 and round(probdist.prob(pred_sentiment), 2)<0.50:
            #print("Ratings calculated")
            rating=3.0
            mylist.update({passkey2:rating})
            
    elif pred_sentiment=="Negative":
        if round(probdist.prob(pred_sentiment), 2)>=0.80:
            #print("Ratings calculated")
            rating=1.0
            mylist.update({passkey2:rating})
            #print("*")
        elif round(probdist.prob(pred_sentiment), 2)<0.80:
            #print("Ratings calculated")
            rating=2.0
            mylist.update({passkey2:rating})
           # print("**")
    x=mycoll.insert_one(mylist)
    y=mycoll.aggregate([{"$group":{"_id":"null", "avgrating":{"$avg":"$Ratings"}}}])
    result=list(y)
    dekh={'id':result[0]['avgrating']}
    

    #return render(request,'check.html',dekh)

    params = {'mypred':pred_sentiment,'myreviews':analyzed,'myrating':mylist['Ratings'],'id':result[0]['avgrating']}
    return render(request,'analyze4.html',params)

def samsung(request):
    return render(request,'samsung.html')
def analyze5(request):
    mycoll=mydb["samsung"]
    def extract_features(word_list):
        return dict([(word, True) for word in word_list])

    #if __name__ == "__main__":\\
    global positive_fileids,negative_fileids
    positive_fileids = movie_reviews.fileids("pos")
    negative_fileids = movie_reviews.fileids("neg")
    features_positive = [
        (extract_features(movie_reviews.words(fileids=[f])), "Positive")
        for f in positive_fileids
    ]
    features_negative = [
        (extract_features(movie_reviews.words(fileids=[f])), "Negative")
        for f in negative_fileids
    ]
    # Split the data into train and test (80/20)
    threshold_factor = 1.0
    threshold_positive = int(threshold_factor * len(features_positive))
    threshold_negative = int(threshold_factor * len(features_negative))
    features_train = (
        features_positive[:threshold_positive] + features_negative[:threshold_negative]
    )
    features_test = (
        features_positive[threshold_positive:] + features_negative[threshold_negative:]
    )
    #print("\nNumber of training datapoints:", len(features_train))
    #print("Number of test datapoints:", len(features_test))
    # Train a Naive Bayes classifier
    classifier = NaiveBayesClassifier.train(features_train)


    djtext = request.GET.get('text', 'default')
    analyzed=djtext
    mylist={}
    key1=("Reviews")
    passkey1=key1
    key2=("Ratings")
    passkey2=key2
    
    input_reviews = [analyzed]
    mylist.update({passkey1:analyzed})
    #print(mylist)
    #print("\nPredictions:")
    for review in input_reviews:
        print("\nReview:", review)
        probdist = classifier.prob_classify(extract_features(review.split()))
        pred_sentiment = probdist.max()
    #print("Predicted sentiment:", pred_sentiment)
    #print("Probability:", round(probdist.prob(pred_sentiment), 2))
    if  pred_sentiment=="Positive":
        if round(probdist.prob(pred_sentiment), 2)>=0.80:
            #print("Ratings calculated")
            rating=5.0
            mylist.update({passkey2:rating})
            
        elif round(probdist.prob(pred_sentiment), 2)>0.70 and round(probdist.prob(pred_sentiment), 2)<0.80:
            #print("Ratings calculated")
            rating=4.0
            mylist.update({passkey2:rating})
           
        elif round(probdist.prob(pred_sentiment), 2)>0.60 and round(probdist.prob(pred_sentiment), 2)<0.50:
            #print("Ratings calculated")
            rating=3.0
            mylist.update({passkey2:rating})
            
    elif pred_sentiment=="Negative":
        if round(probdist.prob(pred_sentiment), 2)>=0.80:
            #print("Ratings calculated")
            rating=1.0
            mylist.update({passkey2:rating})
            #print("*")
        elif round(probdist.prob(pred_sentiment), 2)<0.80:
            #print("Ratings calculated")
            rating=2.0
            mylist.update({passkey2:rating})
           # print("**")
    x=mycoll.insert_one(mylist)
    y=mycoll.aggregate([{"$group":{"_id":"null", "avgrating":{"$avg":"$Ratings"}}}])
    result=list(y)
    dekh={'id':result[0]['avgrating']}
    

    #return render(request,'check.html',dekh)

    params = {'mypred':pred_sentiment,'myreviews':analyzed,'myrating':mylist['Ratings'],'id':result[0]['avgrating']}
    return render(request,'analyze5.html',params)
    
def register(request):

    if request.method == 'POST':
        first_name =request.POST['first_name']
        last_name =request.POST['last_name']
        email =request.POST['email']
        username =request.POST['username']
        password1 =request.POST['password1']
        password2 =request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already exists')
                return redirect('msg')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already exists')
                return redirect('msg')
            else:
                user=User.objects.create_user(username=username,password=password1,first_name=first_name,email=email,last_name=last_name)
                user.save()
                print("user created")

    return render(request,'register.html')

def home(request):
    return render(request,'home.html')
def msg(request):
    return render(request,'msg.html')
def login2(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/home")
        else:
            messages.info(request,'INVALID CREDENTIALS')
            return redirect('msg2')
    return render(request,'login2.html')

def msg2(request):
    return render(request,'msg2.html')
def headphone(request):
    return render(request,'headphone.html')

def boat(request):
    return render(request,'boat.html')
def analyze6(request):
    mycoll=mydb["realmebuds"]
    def extract_features(word_list):
        return dict([(word, True) for word in word_list])

    #if __name__ == "__main__":\\
    global positive_fileids,negative_fileids
    positive_fileids = movie_reviews.fileids("pos")
    negative_fileids = movie_reviews.fileids("neg")
    features_positive = [
        (extract_features(movie_reviews.words(fileids=[f])), "Positive")
        for f in positive_fileids
    ]
    features_negative = [
        (extract_features(movie_reviews.words(fileids=[f])), "Negative")
        for f in negative_fileids
    ]
    # Split the data into train and test (80/20)
    threshold_factor = 1.0
    threshold_positive = int(threshold_factor * len(features_positive))
    threshold_negative = int(threshold_factor * len(features_negative))
    features_train = (
        features_positive[:threshold_positive] + features_negative[:threshold_negative]
    )
    features_test = (
        features_positive[threshold_positive:] + features_negative[threshold_negative:]
    )
    #print("\nNumber of training datapoints:", len(features_train))
    #print("Number of test datapoints:", len(features_test))
    # Train a Naive Bayes classifier
    classifier = NaiveBayesClassifier.train(features_train)


    djtext = request.GET.get('text', 'default')
    analyzed=djtext
    mylist={}
    key1=("Reviews")
    passkey1=key1
    key2=("Ratings")
    passkey2=key2
    
    input_reviews = [analyzed]
    mylist.update({passkey1:analyzed})
    #print(mylist)
    #print("\nPredictions:")
    for review in input_reviews:
        print("\nReview:", review)
        probdist = classifier.prob_classify(extract_features(review.split()))
        pred_sentiment = probdist.max()
    #print("Predicted sentiment:", pred_sentiment)
    #print("Probability:", round(probdist.prob(pred_sentiment), 2))
    if  pred_sentiment=="Positive":
        if round(probdist.prob(pred_sentiment), 2)>=0.80:
            #print("Ratings calculated")
            rating=5.0
            mylist.update({passkey2:rating})
            
        elif round(probdist.prob(pred_sentiment), 2)>0.70 and round(probdist.prob(pred_sentiment), 2)<0.80:
            #print("Ratings calculated")
            rating=4.0
            mylist.update({passkey2:rating})
           
        elif round(probdist.prob(pred_sentiment), 2)>0.60 and round(probdist.prob(pred_sentiment), 2)<0.50:
            #print("Ratings calculated")
            rating=3.0
            mylist.update({passkey2:rating})
            
    elif pred_sentiment=="Negative":
        if round(probdist.prob(pred_sentiment), 2)>=0.80:
            #print("Ratings calculated")
            rating=1.0
            mylist.update({passkey2:rating})
            #print("*")
        elif round(probdist.prob(pred_sentiment), 2)<0.80:
            #print("Ratings calculated")
            rating=2.0
            mylist.update({passkey2:rating})
           # print("**")
    x=mycoll.insert_one(mylist)
    y=mycoll.aggregate([{"$group":{"_id":"null", "avgrating":{"$avg":"$Ratings"}}}])
    result=list(y)
    dekh={'id':result[0]['avgrating']}
    

    #return render(request,'check.html',dekh)

    params = {'mypred':pred_sentiment,'myreviews':analyzed,'myrating':mylist['Ratings'],'id':result[0]['avgrating']}
    return render(request,'analyze6.html',params)

def realmebuds(request):
    return render(request,'realmebuds.html')
def analyze7(request):
    mycoll=mydb["boat"]
    def extract_features(word_list):
        return dict([(word, True) for word in word_list])

    #if __name__ == "__main__":\\
    global positive_fileids,negative_fileids
    positive_fileids = movie_reviews.fileids("pos")
    negative_fileids = movie_reviews.fileids("neg")
    features_positive = [
        (extract_features(movie_reviews.words(fileids=[f])), "Positive")
        for f in positive_fileids
    ]
    features_negative = [
        (extract_features(movie_reviews.words(fileids=[f])), "Negative")
        for f in negative_fileids
    ]
    # Split the data into train and test (80/20)
    threshold_factor = 1.0
    threshold_positive = int(threshold_factor * len(features_positive))
    threshold_negative = int(threshold_factor * len(features_negative))
    features_train = (
        features_positive[:threshold_positive] + features_negative[:threshold_negative]
    )
    features_test = (
        features_positive[threshold_positive:] + features_negative[threshold_negative:]
    )
    #print("\nNumber of training datapoints:", len(features_train))
    #print("Number of test datapoints:", len(features_test))
    # Train a Naive Bayes classifier
    classifier = NaiveBayesClassifier.train(features_train)


    djtext = request.GET.get('text', 'default')
    analyzed=djtext
    mylist={}
    key1=("Reviews")
    passkey1=key1
    key2=("Ratings")
    passkey2=key2
    
    input_reviews = [analyzed]
    mylist.update({passkey1:analyzed})
    #print(mylist)
    #print("\nPredictions:")
    for review in input_reviews:
        print("\nReview:", review)
        probdist = classifier.prob_classify(extract_features(review.split()))
        pred_sentiment = probdist.max()
    #print("Predicted sentiment:", pred_sentiment)
    #print("Probability:", round(probdist.prob(pred_sentiment), 2))
    if  pred_sentiment=="Positive":
        if round(probdist.prob(pred_sentiment), 2)>=0.80:
            #print("Ratings calculated")
            rating=5.0
            mylist.update({passkey2:rating})
            
        elif round(probdist.prob(pred_sentiment), 2)>0.70 and round(probdist.prob(pred_sentiment), 2)<0.80:
            #print("Ratings calculated")
            rating=4.0
            mylist.update({passkey2:rating})
           
        elif round(probdist.prob(pred_sentiment), 2)>0.60 and round(probdist.prob(pred_sentiment), 2)<0.50:
            #print("Ratings calculated")
            rating=3.0
            mylist.update({passkey2:rating})
            
    elif pred_sentiment=="Negative":
        if round(probdist.prob(pred_sentiment), 2)>=0.80:
            #print("Ratings calculated")
            rating=1.0
            mylist.update({passkey2:rating})
            #print("*")
        elif round(probdist.prob(pred_sentiment), 2)<0.80:
            #print("Ratings calculated")
            rating=2.0
            mylist.update({passkey2:rating})
           # print("**")
    x=mycoll.insert_one(mylist)
    y=mycoll.aggregate([{"$group":{"_id":"null", "avgrating":{"$avg":"$Ratings"}}}])
    result=list(y)
    dekh={'id':result[0]['avgrating']}
    

    #return render(request,'check.html',dekh)

    params = {'mypred':pred_sentiment,'myreviews':analyzed,'myrating':mylist['Ratings'],'id':result[0]['avgrating']}
    return render(request,'analyze7.html',params)

def jbl(request):
    return render(request,'jbl.html')
def analyze8(request):
    mycoll=mydb["jbl"]
    def extract_features(word_list):
        return dict([(word, True) for word in word_list])

    #if __name__ == "__main__":\\
    global positive_fileids,negative_fileids
    positive_fileids = movie_reviews.fileids("pos")
    negative_fileids = movie_reviews.fileids("neg")
    features_positive = [
        (extract_features(movie_reviews.words(fileids=[f])), "Positive")
        for f in positive_fileids
    ]
    features_negative = [
        (extract_features(movie_reviews.words(fileids=[f])), "Negative")
        for f in negative_fileids
    ]
    # Split the data into train and test (80/20)
    threshold_factor = 1.0
    threshold_positive = int(threshold_factor * len(features_positive))
    threshold_negative = int(threshold_factor * len(features_negative))
    features_train = (
        features_positive[:threshold_positive] + features_negative[:threshold_negative]
    )
    features_test = (
        features_positive[threshold_positive:] + features_negative[threshold_negative:]
    )
    #print("\nNumber of training datapoints:", len(features_train))
    #print("Number of test datapoints:", len(features_test))
    # Train a Naive Bayes classifier
    classifier = NaiveBayesClassifier.train(features_train)


    djtext = request.GET.get('text', 'default')
    analyzed=djtext
    mylist={}
    key1=("Reviews")
    passkey1=key1
    key2=("Ratings")
    passkey2=key2
    
    input_reviews = [analyzed]
    mylist.update({passkey1:analyzed})
    #print(mylist)
    #print("\nPredictions:")
    for review in input_reviews:
        print("\nReview:", review)
        probdist = classifier.prob_classify(extract_features(review.split()))
        pred_sentiment = probdist.max()
    #print("Predicted sentiment:", pred_sentiment)
    #print("Probability:", round(probdist.prob(pred_sentiment), 2))
    if  pred_sentiment=="Positive":
        if round(probdist.prob(pred_sentiment), 2)>=0.80:
            #print("Ratings calculated")
            rating=5.0
            mylist.update({passkey2:rating})
            
        elif round(probdist.prob(pred_sentiment), 2)>0.70 and round(probdist.prob(pred_sentiment), 2)<0.80:
            #print("Ratings calculated")
            rating=4.0
            mylist.update({passkey2:rating})
           
        elif round(probdist.prob(pred_sentiment), 2)>0.60 and round(probdist.prob(pred_sentiment), 2)<0.50:
            #print("Ratings calculated")
            rating=3.0
            mylist.update({passkey2:rating})
            
    elif pred_sentiment=="Negative":
        if round(probdist.prob(pred_sentiment), 2)>=0.80:
            #print("Ratings calculated")
            rating=1.0
            mylist.update({passkey2:rating})
            #print("*")
        elif round(probdist.prob(pred_sentiment), 2)<0.80:
            #print("Ratings calculated")
            rating=2.0
            mylist.update({passkey2:rating})
           # print("**")
    x=mycoll.insert_one(mylist)
    y=mycoll.aggregate([{"$group":{"_id":"null", "avgrating":{"$avg":"$Ratings"}}}])
    result=list(y)
    dekh={'id':result[0]['avgrating']}
    

    #return render(request,'check.html',dekh)

    params = {'mypred':pred_sentiment,'myreviews':analyzed,'myrating':mylist['Ratings'],'id':result[0]['avgrating']}
    return render(request,'analyze8.html',params)
def skull(request):
    return render(request,'skull.html')
def analyze9(request):
    mycoll=mydb["skull"]
    def extract_features(word_list):
        return dict([(word, True) for word in word_list])

    #if __name__ == "__main__":\\
    global positive_fileids,negative_fileids
    positive_fileids = movie_reviews.fileids("pos")
    negative_fileids = movie_reviews.fileids("neg")
    features_positive = [
        (extract_features(movie_reviews.words(fileids=[f])), "Positive")
        for f in positive_fileids
    ]
    features_negative = [
        (extract_features(movie_reviews.words(fileids=[f])), "Negative")
        for f in negative_fileids
    ]
    # Split the data into train and test (80/20)
    threshold_factor = 1.0
    threshold_positive = int(threshold_factor * len(features_positive))
    threshold_negative = int(threshold_factor * len(features_negative))
    features_train = (
        features_positive[:threshold_positive] + features_negative[:threshold_negative]
    )
    features_test = (
        features_positive[threshold_positive:] + features_negative[threshold_negative:]
    )
    #print("\nNumber of training datapoints:", len(features_train))
    #print("Number of test datapoints:", len(features_test))
    # Train a Naive Bayes classifier
    classifier = NaiveBayesClassifier.train(features_train)


    djtext = request.GET.get('text', 'default')
    analyzed=djtext
    mylist={}
    key1=("Reviews")
    passkey1=key1
    key2=("Ratings")
    passkey2=key2
    
    input_reviews = [analyzed]
    mylist.update({passkey1:analyzed})
    #print(mylist)
    #print("\nPredictions:")
    for review in input_reviews:
        print("\nReview:", review)
        probdist = classifier.prob_classify(extract_features(review.split()))
        pred_sentiment = probdist.max()
    #print("Predicted sentiment:", pred_sentiment)
    #print("Probability:", round(probdist.prob(pred_sentiment), 2))
    if  pred_sentiment=="Positive":
        if round(probdist.prob(pred_sentiment), 2)>=0.80:
            #print("Ratings calculated")
            rating=5.0
            mylist.update({passkey2:rating})
            
        elif round(probdist.prob(pred_sentiment), 2)>0.70 and round(probdist.prob(pred_sentiment), 2)<0.80:
            #print("Ratings calculated")
            rating=4.0
            mylist.update({passkey2:rating})
           
        elif round(probdist.prob(pred_sentiment), 2)>0.60 and round(probdist.prob(pred_sentiment), 2)<0.50:
            #print("Ratings calculated")
            rating=3.0
            mylist.update({passkey2:rating})
            
    elif pred_sentiment=="Negative":
        if round(probdist.prob(pred_sentiment), 2)>=0.80:
            #print("Ratings calculated")
            rating=1.0
            mylist.update({passkey2:rating})
            #print("*")
        elif round(probdist.prob(pred_sentiment), 2)<0.80:
            #print("Ratings calculated")
            rating=2.0
            mylist.update({passkey2:rating})
           # print("**")
    x=mycoll.insert_one(mylist)
    y=mycoll.aggregate([{"$group":{"_id":"null", "avgrating":{"$avg":"$Ratings"}}}])
    result=list(y)
    dekh={'id':result[0]['avgrating']}
    

    #return render(request,'check.html',dekh)

    params = {'mypred':pred_sentiment,'myreviews':analyzed,'myrating':mylist['Ratings'],'id':result[0]['avgrating']}
    return render(request,'analyze9.html',params)
def sony(request):
    return render(request,'sony.html')
def analyze10(request):
    mycoll=mydb["sony"]
    def extract_features(word_list):
        return dict([(word, True) for word in word_list])

    #if __name__ == "__main__":\\
    global positive_fileids,negative_fileids
    positive_fileids = movie_reviews.fileids("pos")
    negative_fileids = movie_reviews.fileids("neg")
    features_positive = [
        (extract_features(movie_reviews.words(fileids=[f])), "Positive")
        for f in positive_fileids
    ]
    features_negative = [
        (extract_features(movie_reviews.words(fileids=[f])), "Negative")
        for f in negative_fileids
    ]
    # Split the data into train and test (80/20)
    threshold_factor = 1.0
    threshold_positive = int(threshold_factor * len(features_positive))
    threshold_negative = int(threshold_factor * len(features_negative))
    features_train = (
        features_positive[:threshold_positive] + features_negative[:threshold_negative]
    )
    features_test = (
        features_positive[threshold_positive:] + features_negative[threshold_negative:]
    )
    #print("\nNumber of training datapoints:", len(features_train))
    #print("Number of test datapoints:", len(features_test))
    # Train a Naive Bayes classifier
    classifier = NaiveBayesClassifier.train(features_train)


    djtext = request.GET.get('text', 'default')
    analyzed=djtext
    mylist={}
    key1=("Reviews")
    passkey1=key1
    key2=("Ratings")
    passkey2=key2
    
    input_reviews = [analyzed]
    mylist.update({passkey1:analyzed})
    #print(mylist)
    #print("\nPredictions:")
    for review in input_reviews:
        print("\nReview:", review)
        probdist = classifier.prob_classify(extract_features(review.split()))
        pred_sentiment = probdist.max()
    #print("Predicted sentiment:", pred_sentiment)
    #print("Probability:", round(probdist.prob(pred_sentiment), 2))
    if  pred_sentiment=="Positive":
        if round(probdist.prob(pred_sentiment), 2)>=0.80:
            #print("Ratings calculated")
            rating=5.0
            mylist.update({passkey2:rating})
            
        elif round(probdist.prob(pred_sentiment), 2)>0.70 and round(probdist.prob(pred_sentiment), 2)<0.80:
            #print("Ratings calculated")
            rating=4.0
            mylist.update({passkey2:rating})
           
        elif round(probdist.prob(pred_sentiment), 2)>0.60 and round(probdist.prob(pred_sentiment), 2)<0.50:
            #print("Ratings calculated")
            rating=3.0
            mylist.update({passkey2:rating})
            
    elif pred_sentiment=="Negative":
        if round(probdist.prob(pred_sentiment), 2)>=0.80:
            #print("Ratings calculated")
            rating=1.0
            mylist.update({passkey2:rating})
            #print("*")
        elif round(probdist.prob(pred_sentiment), 2)<0.80:
            #print("Ratings calculated")
            rating=2.0
            mylist.update({passkey2:rating})
           # print("**")
    x=mycoll.insert_one(mylist)
    y=mycoll.aggregate([{"$group":{"_id":"null", "avgrating":{"$avg":"$Ratings"}}}])
    result=list(y)
    dekh={'id':result[0]['avgrating']}
    

    #return render(request,'check.html',dekh)

    params = {'mypred':pred_sentiment,'myreviews':analyzed,'myrating':mylist['Ratings'],'id':result[0]['avgrating']}
    return render(request,'analyze10.html',params)


def laptop(request):
    return render(request,'laptop.html')

def dell(request):
    return render(request,'dell.html')
def analyze11(request):
    mycoll=mydb["dell"]
    def extract_features(word_list):
        return dict([(word, True) for word in word_list])

    #if __name__ == "__main__":\\
    global positive_fileids,negative_fileids
    positive_fileids = movie_reviews.fileids("pos")
    negative_fileids = movie_reviews.fileids("neg")
    features_positive = [
        (extract_features(movie_reviews.words(fileids=[f])), "Positive")
        for f in positive_fileids
    ]
    features_negative = [
        (extract_features(movie_reviews.words(fileids=[f])), "Negative")
        for f in negative_fileids
    ]
    # Split the data into train and test (80/20)
    threshold_factor = 1.0
    threshold_positive = int(threshold_factor * len(features_positive))
    threshold_negative = int(threshold_factor * len(features_negative))
    features_train = (
        features_positive[:threshold_positive] + features_negative[:threshold_negative]
    )
    features_test = (
        features_positive[threshold_positive:] + features_negative[threshold_negative:]
    )
    #print("\nNumber of training datapoints:", len(features_train))
    #print("Number of test datapoints:", len(features_test))
    # Train a Naive Bayes classifier
    classifier = NaiveBayesClassifier.train(features_train)


    djtext = request.GET.get('text', 'default')
    analyzed=djtext
    mylist={}
    key1=("Reviews")
    passkey1=key1
    key2=("Ratings")
    passkey2=key2
    
    input_reviews = [analyzed]
    mylist.update({passkey1:analyzed})
    #print(mylist)
    #print("\nPredictions:")
    for review in input_reviews:
        print("\nReview:", review)
        probdist = classifier.prob_classify(extract_features(review.split()))
        pred_sentiment = probdist.max()
    #print("Predicted sentiment:", pred_sentiment)
    #print("Probability:", round(probdist.prob(pred_sentiment), 2))
    if  pred_sentiment=="Positive":
        if round(probdist.prob(pred_sentiment), 2)>=0.80:
            #print("Ratings calculated")
            rating=5.0
            mylist.update({passkey2:rating})
            
        elif round(probdist.prob(pred_sentiment), 2)>0.70 and round(probdist.prob(pred_sentiment), 2)<0.80:
            #print("Ratings calculated")
            rating=4.0
            mylist.update({passkey2:rating})
           
        elif round(probdist.prob(pred_sentiment), 2)>0.60 and round(probdist.prob(pred_sentiment), 2)<0.50:
            #print("Ratings calculated")
            rating=3.0
            mylist.update({passkey2:rating})
            
    elif pred_sentiment=="Negative":
        if round(probdist.prob(pred_sentiment), 2)>=0.80:
            #print("Ratings calculated")
            rating=1.0
            mylist.update({passkey2:rating})
            #print("*")
        elif round(probdist.prob(pred_sentiment), 2)<0.80:
            #print("Ratings calculated")
            rating=2.0
            mylist.update({passkey2:rating})
           # print("**")
    x=mycoll.insert_one(mylist)
    y=mycoll.aggregate([{"$group":{"_id":"null", "avgrating":{"$avg":"$Ratings"}}}])
    result=list(y)
    dekh={'id':result[0]['avgrating']}
    

    #return render(request,'check.html',dekh)

    params = {'mypred':pred_sentiment,'myreviews':analyzed,'myrating':mylist['Ratings'],'id':result[0]['avgrating']}
    return render(request,'analyze11.html',params)
def hp(request):
    return render(request,'hp.html')
def analyze12(request):
    mycoll=mydb["hp"]
    def extract_features(word_list):
        return dict([(word, True) for word in word_list])

    #if __name__ == "__main__":\\
    global positive_fileids,negative_fileids
    positive_fileids = movie_reviews.fileids("pos")
    negative_fileids = movie_reviews.fileids("neg")
    features_positive = [
        (extract_features(movie_reviews.words(fileids=[f])), "Positive")
        for f in positive_fileids
    ]
    features_negative = [
        (extract_features(movie_reviews.words(fileids=[f])), "Negative")
        for f in negative_fileids
    ]
    # Split the data into train and test (80/20)
    threshold_factor = 1.0
    threshold_positive = int(threshold_factor * len(features_positive))
    threshold_negative = int(threshold_factor * len(features_negative))
    features_train = (
        features_positive[:threshold_positive] + features_negative[:threshold_negative]
    )
    features_test = (
        features_positive[threshold_positive:] + features_negative[threshold_negative:]
    )
    #print("\nNumber of training datapoints:", len(features_train))
    #print("Number of test datapoints:", len(features_test))
    # Train a Naive Bayes classifier
    classifier = NaiveBayesClassifier.train(features_train)


    djtext = request.GET.get('text', 'default')
    analyzed=djtext
    mylist={}
    key1=("Reviews")
    passkey1=key1
    key2=("Ratings")
    passkey2=key2
    
    input_reviews = [analyzed]
    mylist.update({passkey1:analyzed})
    #print(mylist)
    #print("\nPredictions:")
    for review in input_reviews:
        print("\nReview:", review)
        probdist = classifier.prob_classify(extract_features(review.split()))
        pred_sentiment = probdist.max()
    #print("Predicted sentiment:", pred_sentiment)
    #print("Probability:", round(probdist.prob(pred_sentiment), 2))
    if  pred_sentiment=="Positive":
        if round(probdist.prob(pred_sentiment), 2)>=0.80:
            #print("Ratings calculated")
            rating=5.0
            mylist.update({passkey2:rating})
            
        elif round(probdist.prob(pred_sentiment), 2)>0.70 and round(probdist.prob(pred_sentiment), 2)<0.80:
            #print("Ratings calculated")
            rating=4.0
            mylist.update({passkey2:rating})
           
        elif round(probdist.prob(pred_sentiment), 2)>0.60 and round(probdist.prob(pred_sentiment), 2)<0.50:
            #print("Ratings calculated")
            rating=3.0
            mylist.update({passkey2:rating})
            
    elif pred_sentiment=="Negative":
        if round(probdist.prob(pred_sentiment), 2)>=0.80:
            #print("Ratings calculated")
            rating=1.0
            mylist.update({passkey2:rating})
            #print("*")
        elif round(probdist.prob(pred_sentiment), 2)<0.80:
            #print("Ratings calculated")
            rating=2.0
            mylist.update({passkey2:rating})
           # print("**")
    x=mycoll.insert_one(mylist)
    y=mycoll.aggregate([{"$group":{"_id":"null", "avgrating":{"$avg":"$Ratings"}}}])
    result=list(y)
    dekh={'id':result[0]['avgrating']}
    

    #return render(request,'check.html',dekh)

    params = {'mypred':pred_sentiment,'myreviews':analyzed,'myrating':mylist['Ratings'],'id':result[0]['avgrating']}
    return render(request,'analyze12.html',params)
def msi(request):
    return render(request,'msi.html')
def analyze13(request):
    mycoll=mydb["msi"]
    def extract_features(word_list):
        return dict([(word, True) for word in word_list])

    #if __name__ == "__main__":\\
    global positive_fileids,negative_fileids
    positive_fileids = movie_reviews.fileids("pos")
    negative_fileids = movie_reviews.fileids("neg")
    features_positive = [
        (extract_features(movie_reviews.words(fileids=[f])), "Positive")
        for f in positive_fileids
    ]
    features_negative = [
        (extract_features(movie_reviews.words(fileids=[f])), "Negative")
        for f in negative_fileids
    ]
    # Split the data into train and test (80/20)
    threshold_factor = 1.0
    threshold_positive = int(threshold_factor * len(features_positive))
    threshold_negative = int(threshold_factor * len(features_negative))
    features_train = (
        features_positive[:threshold_positive] + features_negative[:threshold_negative]
    )
    features_test = (
        features_positive[threshold_positive:] + features_negative[threshold_negative:]
    )
    #print("\nNumber of training datapoints:", len(features_train))
    #print("Number of test datapoints:", len(features_test))
    # Train a Naive Bayes classifier
    classifier = NaiveBayesClassifier.train(features_train)


    djtext = request.GET.get('text', 'default')
    analyzed=djtext
    mylist={}
    key1=("Reviews")
    passkey1=key1
    key2=("Ratings")
    passkey2=key2
    
    input_reviews = [analyzed]
    mylist.update({passkey1:analyzed})
    #print(mylist)
    #print("\nPredictions:")
    for review in input_reviews:
        print("\nReview:", review)
        probdist = classifier.prob_classify(extract_features(review.split()))
        pred_sentiment = probdist.max()
    #print("Predicted sentiment:", pred_sentiment)
    #print("Probability:", round(probdist.prob(pred_sentiment), 2))
    if  pred_sentiment=="Positive":
        if round(probdist.prob(pred_sentiment), 2)>=0.80:
            #print("Ratings calculated")
            rating=5.0
            mylist.update({passkey2:rating})
            
        elif round(probdist.prob(pred_sentiment), 2)>0.70 and round(probdist.prob(pred_sentiment), 2)<0.80:
            #print("Ratings calculated")
            rating=4.0
            mylist.update({passkey2:rating})
           
        elif round(probdist.prob(pred_sentiment), 2)>0.60 and round(probdist.prob(pred_sentiment), 2)<0.50:
            #print("Ratings calculated")
            rating=3.0
            mylist.update({passkey2:rating})
            
    elif pred_sentiment=="Negative":
        if round(probdist.prob(pred_sentiment), 2)>=0.80:
            #print("Ratings calculated")
            rating=1.0
            mylist.update({passkey2:rating})
            #print("*")
        elif round(probdist.prob(pred_sentiment), 2)<0.80:
            #print("Ratings calculated")
            rating=2.0
            mylist.update({passkey2:rating})
           # print("**")
    x=mycoll.insert_one(mylist)
    y=mycoll.aggregate([{"$group":{"_id":"null", "avgrating":{"$avg":"$Ratings"}}}])
    result=list(y)
    dekh={'id':result[0]['avgrating']}
    

    #return render(request,'check.html',dekh)

    params = {'mypred':pred_sentiment,'myreviews':analyzed,'myrating':mylist['Ratings'],'id':result[0]['avgrating']}
    return render(request,'analyze13.html',params)
def roglaptop(request):
    return render(request,'roglaptop.html')
def analyze14(request):
    mycoll=mydb["roglaptop"]
    def extract_features(word_list):
        return dict([(word, True) for word in word_list])

    #if __name__ == "__main__":\\
    global positive_fileids,negative_fileids
    positive_fileids = movie_reviews.fileids("pos")
    negative_fileids = movie_reviews.fileids("neg")
    features_positive = [
        (extract_features(movie_reviews.words(fileids=[f])), "Positive")
        for f in positive_fileids
    ]
    features_negative = [
        (extract_features(movie_reviews.words(fileids=[f])), "Negative")
        for f in negative_fileids
    ]
    # Split the data into train and test (80/20)
    threshold_factor = 1.0
    threshold_positive = int(threshold_factor * len(features_positive))
    threshold_negative = int(threshold_factor * len(features_negative))
    features_train = (
        features_positive[:threshold_positive] + features_negative[:threshold_negative]
    )
    features_test = (
        features_positive[threshold_positive:] + features_negative[threshold_negative:]
    )
    #print("\nNumber of training datapoints:", len(features_train))
    #print("Number of test datapoints:", len(features_test))
    # Train a Naive Bayes classifier
    classifier = NaiveBayesClassifier.train(features_train)


    djtext = request.GET.get('text', 'default')
    analyzed=djtext
    mylist={}
    key1=("Reviews")
    passkey1=key1
    key2=("Ratings")
    passkey2=key2
    
    input_reviews = [analyzed]
    mylist.update({passkey1:analyzed})
    #print(mylist)
    #print("\nPredictions:")
    for review in input_reviews:
        print("\nReview:", review)
        probdist = classifier.prob_classify(extract_features(review.split()))
        pred_sentiment = probdist.max()
    #print("Predicted sentiment:", pred_sentiment)
    #print("Probability:", round(probdist.prob(pred_sentiment), 2))
    if  pred_sentiment=="Positive":
        if round(probdist.prob(pred_sentiment), 2)>=0.80:
            #print("Ratings calculated")
            rating=5.0
            mylist.update({passkey2:rating})
            
        elif round(probdist.prob(pred_sentiment), 2)>0.70 and round(probdist.prob(pred_sentiment), 2)<0.80:
            #print("Ratings calculated")
            rating=4.0
            mylist.update({passkey2:rating})
           
        elif round(probdist.prob(pred_sentiment), 2)>0.60 and round(probdist.prob(pred_sentiment), 2)<0.50:
            #print("Ratings calculated")
            rating=3.0
            mylist.update({passkey2:rating})
            
    elif pred_sentiment=="Negative":
        if round(probdist.prob(pred_sentiment), 2)>=0.80:
            #print("Ratings calculated")
            rating=1.0
            mylist.update({passkey2:rating})
            #print("*")
        elif round(probdist.prob(pred_sentiment), 2)<0.80:
            #print("Ratings calculated")
            rating=2.0
            mylist.update({passkey2:rating})
           # print("**")
    x=mycoll.insert_one(mylist)
    y=mycoll.aggregate([{"$group":{"_id":"null", "avgrating":{"$avg":"$Ratings"}}}])
    result=list(y)
    dekh={'id':result[0]['avgrating']}
    

    #return render(request,'check.html',dekh)

    params = {'mypred':pred_sentiment,'myreviews':analyzed,'myrating':mylist['Ratings'],'id':result[0]['avgrating']}
    return render(request,'analyze14.html',params)
def mac(request):
    return render(request,'mac.html')
def analyze15(request):
    mycoll=mydb["mac"]
    def extract_features(word_list):
        return dict([(word, True) for word in word_list])

    #if __name__ == "__main__":\\
    global positive_fileids,negative_fileids
    positive_fileids = movie_reviews.fileids("pos")
    negative_fileids = movie_reviews.fileids("neg")
    features_positive = [
        (extract_features(movie_reviews.words(fileids=[f])), "Positive")
        for f in positive_fileids
    ]
    features_negative = [
        (extract_features(movie_reviews.words(fileids=[f])), "Negative")
        for f in negative_fileids
    ]
    # Split the data into train and test (80/20)
    threshold_factor = 1.0
    threshold_positive = int(threshold_factor * len(features_positive))
    threshold_negative = int(threshold_factor * len(features_negative))
    features_train = (
        features_positive[:threshold_positive] + features_negative[:threshold_negative]
    )
    features_test = (
        features_positive[threshold_positive:] + features_negative[threshold_negative:]
    )
    #print("\nNumber of training datapoints:", len(features_train))
    #print("Number of test datapoints:", len(features_test))
    # Train a Naive Bayes classifier
    classifier = NaiveBayesClassifier.train(features_train)


    djtext = request.GET.get('text', 'default')
    analyzed=djtext
    mylist={}
    key1=("Reviews")
    passkey1=key1
    key2=("Ratings")
    passkey2=key2
    
    input_reviews = [analyzed]
    mylist.update({passkey1:analyzed})
    #print(mylist)
    #print("\nPredictions:")
    for review in input_reviews:
        print("\nReview:", review)
        probdist = classifier.prob_classify(extract_features(review.split()))
        pred_sentiment = probdist.max()
    #print("Predicted sentiment:", pred_sentiment)
    #print("Probability:", round(probdist.prob(pred_sentiment), 2))
    if  pred_sentiment=="Positive":
        if round(probdist.prob(pred_sentiment), 2)>=0.80:
            #print("Ratings calculated")
            rating=5.0
            mylist.update({passkey2:rating})
            
        elif round(probdist.prob(pred_sentiment), 2)>0.70 and round(probdist.prob(pred_sentiment), 2)<0.80:
            #print("Ratings calculated")
            rating=4.0
            mylist.update({passkey2:rating})
           
        elif round(probdist.prob(pred_sentiment), 2)>0.60 and round(probdist.prob(pred_sentiment), 2)<0.50:
            #print("Ratings calculated")
            rating=3.0
            mylist.update({passkey2:rating})
            
    elif pred_sentiment=="Negative":
        if round(probdist.prob(pred_sentiment), 2)>=0.80:
            #print("Ratings calculated")
            rating=1.0
            mylist.update({passkey2:rating})
            #print("*")
        elif round(probdist.prob(pred_sentiment), 2)<0.80:
            #print("Ratings calculated")
            rating=2.0
            mylist.update({passkey2:rating})
           # print("**")
    x=mycoll.insert_one(mylist)
    y=mycoll.aggregate([{"$group":{"_id":"null", "avgrating":{"$avg":"$Ratings"}}}])
    result=list(y)
    dekh={'id':result[0]['avgrating']}
    

    #return render(request,'check.html',dekh)

    params = {'mypred':pred_sentiment,'myreviews':analyzed,'myrating':mylist['Ratings'],'id':result[0]['avgrating']}
    return render(request,'analyze15.html',params)

def tv(request):
    return render(request,'tv.html')
def samtv(request):
    return render(request,'samtv.html')
def analyze16(request):
    mycoll=mydb["samtv"]
    def extract_features(word_list):
        return dict([(word, True) for word in word_list])

    #if __name__ == "__main__":\\
    global positive_fileids,negative_fileids
    positive_fileids = movie_reviews.fileids("pos")
    negative_fileids = movie_reviews.fileids("neg")
    features_positive = [
        (extract_features(movie_reviews.words(fileids=[f])), "Positive")
        for f in positive_fileids
    ]
    features_negative = [
        (extract_features(movie_reviews.words(fileids=[f])), "Negative")
        for f in negative_fileids
    ]
    # Split the data into train and test (80/20)
    threshold_factor = 1.0
    threshold_positive = int(threshold_factor * len(features_positive))
    threshold_negative = int(threshold_factor * len(features_negative))
    features_train = (
        features_positive[:threshold_positive] + features_negative[:threshold_negative]
    )
    features_test = (
        features_positive[threshold_positive:] + features_negative[threshold_negative:]
    )
    #print("\nNumber of training datapoints:", len(features_train))
    #print("Number of test datapoints:", len(features_test))
    # Train a Naive Bayes classifier
    classifier = NaiveBayesClassifier.train(features_train)


    djtext = request.GET.get('text', 'default')
    analyzed=djtext
    mylist={}
    key1=("Reviews")
    passkey1=key1
    key2=("Ratings")
    passkey2=key2
    
    input_reviews = [analyzed]
    mylist.update({passkey1:analyzed})
    #print(mylist)
    #print("\nPredictions:")
    for review in input_reviews:
        print("\nReview:", review)
        probdist = classifier.prob_classify(extract_features(review.split()))
        pred_sentiment = probdist.max()
    #print("Predicted sentiment:", pred_sentiment)
    #print("Probability:", round(probdist.prob(pred_sentiment), 2))
    if  pred_sentiment=="Positive":
        if round(probdist.prob(pred_sentiment), 2)>=0.80:
            #print("Ratings calculated")
            rating=5.0
            mylist.update({passkey2:rating})
            
        elif round(probdist.prob(pred_sentiment), 2)>0.70 and round(probdist.prob(pred_sentiment), 2)<0.80:
            #print("Ratings calculated")
            rating=4.0
            mylist.update({passkey2:rating})
           
        elif round(probdist.prob(pred_sentiment), 2)>0.60 and round(probdist.prob(pred_sentiment), 2)<0.50:
            #print("Ratings calculated")
            rating=3.0
            mylist.update({passkey2:rating})
            
    elif pred_sentiment=="Negative":
        if round(probdist.prob(pred_sentiment), 2)>=0.80:
            #print("Ratings calculated")
            rating=1.0
            mylist.update({passkey2:rating})
            #print("*")
        elif round(probdist.prob(pred_sentiment), 2)<0.80:
            #print("Ratings calculated")
            rating=2.0
            mylist.update({passkey2:rating})
           # print("**")
    x=mycoll.insert_one(mylist)
    y=mycoll.aggregate([{"$group":{"_id":"null", "avgrating":{"$avg":"$Ratings"}}}])
    result=list(y)
    dekh={'id':result[0]['avgrating']}
    

    #return render(request,'check.html',dekh)

    params = {'mypred':pred_sentiment,'myreviews':analyzed,'myrating':mylist['Ratings'],'id':result[0]['avgrating']}
    return render(request,'analyze16.html',params)
def mitv(request):
    return render(request,'mitv.html')
def analyze17(request):
    mycoll=mydb["mitv"]
    def extract_features(word_list):
        return dict([(word, True) for word in word_list])

    #if __name__ == "__main__":\\
    global positive_fileids,negative_fileids
    positive_fileids = movie_reviews.fileids("pos")
    negative_fileids = movie_reviews.fileids("neg")
    features_positive = [
        (extract_features(movie_reviews.words(fileids=[f])), "Positive")
        for f in positive_fileids
    ]
    features_negative = [
        (extract_features(movie_reviews.words(fileids=[f])), "Negative")
        for f in negative_fileids
    ]
    # Split the data into train and test (80/20)
    threshold_factor = 1.0
    threshold_positive = int(threshold_factor * len(features_positive))
    threshold_negative = int(threshold_factor * len(features_negative))
    features_train = (
        features_positive[:threshold_positive] + features_negative[:threshold_negative]
    )
    features_test = (
        features_positive[threshold_positive:] + features_negative[threshold_negative:]
    )
    #print("\nNumber of training datapoints:", len(features_train))
    #print("Number of test datapoints:", len(features_test))
    # Train a Naive Bayes classifier
    classifier = NaiveBayesClassifier.train(features_train)


    djtext = request.GET.get('text', 'default')
    analyzed=djtext
    mylist={}
    key1=("Reviews")
    passkey1=key1
    key2=("Ratings")
    passkey2=key2
    
    input_reviews = [analyzed]
    mylist.update({passkey1:analyzed})
    #print(mylist)
    #print("\nPredictions:")
    for review in input_reviews:
        print("\nReview:", review)
        probdist = classifier.prob_classify(extract_features(review.split()))
        pred_sentiment = probdist.max()
    #print("Predicted sentiment:", pred_sentiment)
    #print("Probability:", round(probdist.prob(pred_sentiment), 2))
    if  pred_sentiment=="Positive":
        if round(probdist.prob(pred_sentiment), 2)>=0.80:
            #print("Ratings calculated")
            rating=5.0
            mylist.update({passkey2:rating})
            
        elif round(probdist.prob(pred_sentiment), 2)>0.70 and round(probdist.prob(pred_sentiment), 2)<0.80:
            #print("Ratings calculated")
            rating=4.0
            mylist.update({passkey2:rating})
           
        elif round(probdist.prob(pred_sentiment), 2)>0.60 and round(probdist.prob(pred_sentiment), 2)<0.50:
            #print("Ratings calculated")
            rating=3.0
            mylist.update({passkey2:rating})
            
    elif pred_sentiment=="Negative":
        if round(probdist.prob(pred_sentiment), 2)>=0.80:
            #print("Ratings calculated")
            rating=1.0
            mylist.update({passkey2:rating})
            #print("*")
        elif round(probdist.prob(pred_sentiment), 2)<0.80:
            #print("Ratings calculated")
            rating=2.0
            mylist.update({passkey2:rating})
           # print("**")
    x=mycoll.insert_one(mylist)
    y=mycoll.aggregate([{"$group":{"_id":"null", "avgrating":{"$avg":"$Ratings"}}}])
    result=list(y)
    dekh={'id':result[0]['avgrating']}
    

    #return render(request,'check.html',dekh)

    params = {'mypred':pred_sentiment,'myreviews':analyzed,'myrating':mylist['Ratings'],'id':result[0]['avgrating']}
    return render(request,'analyze17.html',params)
def onetv(request):
    return render(request,'onetv.html')
def analyze18(request):
    mycoll=mydb["oneplustv"]
    def extract_features(word_list):
        return dict([(word, True) for word in word_list])

    #if __name__ == "__main__":\\
    global positive_fileids,negative_fileids
    positive_fileids = movie_reviews.fileids("pos")
    negative_fileids = movie_reviews.fileids("neg")
    features_positive = [
        (extract_features(movie_reviews.words(fileids=[f])), "Positive")
        for f in positive_fileids
    ]
    features_negative = [
        (extract_features(movie_reviews.words(fileids=[f])), "Negative")
        for f in negative_fileids
    ]
    # Split the data into train and test (80/20)
    threshold_factor = 1.0
    threshold_positive = int(threshold_factor * len(features_positive))
    threshold_negative = int(threshold_factor * len(features_negative))
    features_train = (
        features_positive[:threshold_positive] + features_negative[:threshold_negative]
    )
    features_test = (
        features_positive[threshold_positive:] + features_negative[threshold_negative:]
    )
    #print("\nNumber of training datapoints:", len(features_train))
    #print("Number of test datapoints:", len(features_test))
    # Train a Naive Bayes classifier
    classifier = NaiveBayesClassifier.train(features_train)


    djtext = request.GET.get('text', 'default')
    analyzed=djtext
    mylist={}
    key1=("Reviews")
    passkey1=key1
    key2=("Ratings")
    passkey2=key2
    
    input_reviews = [analyzed]
    mylist.update({passkey1:analyzed})
    #print(mylist)
    #print("\nPredictions:")
    for review in input_reviews:
        print("\nReview:", review)
        probdist = classifier.prob_classify(extract_features(review.split()))
        pred_sentiment = probdist.max()
    #print("Predicted sentiment:", pred_sentiment)
    #print("Probability:", round(probdist.prob(pred_sentiment), 2))
    if  pred_sentiment=="Positive":
        if round(probdist.prob(pred_sentiment), 2)>=0.80:
            #print("Ratings calculated")
            rating=5.0
            mylist.update({passkey2:rating})
            
        elif round(probdist.prob(pred_sentiment), 2)>0.70 and round(probdist.prob(pred_sentiment), 2)<0.80:
            #print("Ratings calculated")
            rating=4.0
            mylist.update({passkey2:rating})
           
        elif round(probdist.prob(pred_sentiment), 2)>0.60 and round(probdist.prob(pred_sentiment), 2)<0.50:
            #print("Ratings calculated")
            rating=3.0
            mylist.update({passkey2:rating})
            
    elif pred_sentiment=="Negative":
        if round(probdist.prob(pred_sentiment), 2)>=0.80:
            #print("Ratings calculated")
            rating=1.0
            mylist.update({passkey2:rating})
            #print("*")
        elif round(probdist.prob(pred_sentiment), 2)<0.80:
            #print("Ratings calculated")
            rating=2.0
            mylist.update({passkey2:rating})
           # print("**")
    x=mycoll.insert_one(mylist)
    y=mycoll.aggregate([{"$group":{"_id":"null", "avgrating":{"$avg":"$Ratings"}}}])
    result=list(y)
    dekh={'id':result[0]['avgrating']}
    

    #return render(request,'check.html',dekh)

    params = {'mypred':pred_sentiment,'myreviews':analyzed,'myrating':mylist['Ratings'],'id':result[0]['avgrating']}
    return render(request,'analyze18.html',params)
def lg(request):
    return render(request,'lg.html')
def analyze19(request):
    mycoll=mydb["lgtv"]
    def extract_features(word_list):
        return dict([(word, True) for word in word_list])

    #if __name__ == "__main__":\\
    global positive_fileids,negative_fileids
    positive_fileids = movie_reviews.fileids("pos")
    negative_fileids = movie_reviews.fileids("neg")
    features_positive = [
        (extract_features(movie_reviews.words(fileids=[f])), "Positive")
        for f in positive_fileids
    ]
    features_negative = [
        (extract_features(movie_reviews.words(fileids=[f])), "Negative")
        for f in negative_fileids
    ]
    # Split the data into train and test (80/20)
    threshold_factor = 1.0
    threshold_positive = int(threshold_factor * len(features_positive))
    threshold_negative = int(threshold_factor * len(features_negative))
    features_train = (
        features_positive[:threshold_positive] + features_negative[:threshold_negative]
    )
    features_test = (
        features_positive[threshold_positive:] + features_negative[threshold_negative:]
    )
    #print("\nNumber of training datapoints:", len(features_train))
    #print("Number of test datapoints:", len(features_test))
    # Train a Naive Bayes classifier
    classifier = NaiveBayesClassifier.train(features_train)


    djtext = request.GET.get('text', 'default')
    analyzed=djtext
    mylist={}
    key1=("Reviews")
    passkey1=key1
    key2=("Ratings")
    passkey2=key2
    
    input_reviews = [analyzed]
    mylist.update({passkey1:analyzed})
    #print(mylist)
    #print("\nPredictions:")
    for review in input_reviews:
        print("\nReview:", review)
        probdist = classifier.prob_classify(extract_features(review.split()))
        pred_sentiment = probdist.max()
    #print("Predicted sentiment:", pred_sentiment)
    #print("Probability:", round(probdist.prob(pred_sentiment), 2))
    if  pred_sentiment=="Positive":
        if round(probdist.prob(pred_sentiment), 2)>=0.80:
            #print("Ratings calculated")
            rating=5.0
            mylist.update({passkey2:rating})
            
        elif round(probdist.prob(pred_sentiment), 2)>0.70 and round(probdist.prob(pred_sentiment), 2)<0.80:
            #print("Ratings calculated")
            rating=4.0
            mylist.update({passkey2:rating})
           
        elif round(probdist.prob(pred_sentiment), 2)>0.60 and round(probdist.prob(pred_sentiment), 2)<0.50:
            #print("Ratings calculated")
            rating=3.0
            mylist.update({passkey2:rating})
            
    elif pred_sentiment=="Negative":
        if round(probdist.prob(pred_sentiment), 2)>=0.80:
            #print("Ratings calculated")
            rating=1.0
            mylist.update({passkey2:rating})
            #print("*")
        elif round(probdist.prob(pred_sentiment), 2)<0.80:
            #print("Ratings calculated")
            rating=2.0
            mylist.update({passkey2:rating})
           # print("**")
    x=mycoll.insert_one(mylist)
    y=mycoll.aggregate([{"$group":{"_id":"null", "avgrating":{"$avg":"$Ratings"}}}])
    result=list(y)
    dekh={'id':result[0]['avgrating']}
    

    #return render(request,'check.html',dekh)

    params = {'mypred':pred_sentiment,'myreviews':analyzed,'myrating':mylist['Ratings'],'id':result[0]['avgrating']}
    return render(request,'analyze19.html',params)
def sonytv(request):
    return render(request,'sonytv.html')
def analyze20(request):
    mycoll=mydb["sonytv"]
    def extract_features(word_list):
        return dict([(word, True) for word in word_list])

    #if __name__ == "__main__":\\
    global positive_fileids,negative_fileids
    positive_fileids = movie_reviews.fileids("pos")
    negative_fileids = movie_reviews.fileids("neg")
    features_positive = [
        (extract_features(movie_reviews.words(fileids=[f])), "Positive")
        for f in positive_fileids
    ]
    features_negative = [
        (extract_features(movie_reviews.words(fileids=[f])), "Negative")
        for f in negative_fileids
    ]
    # Split the data into train and test (80/20)
    threshold_factor = 1.0
    threshold_positive = int(threshold_factor * len(features_positive))
    threshold_negative = int(threshold_factor * len(features_negative))
    features_train = (
        features_positive[:threshold_positive] + features_negative[:threshold_negative]
    )
    features_test = (
        features_positive[threshold_positive:] + features_negative[threshold_negative:]
    )
    #print("\nNumber of training datapoints:", len(features_train))
    #print("Number of test datapoints:", len(features_test))
    # Train a Naive Bayes classifier
    classifier = NaiveBayesClassifier.train(features_train)


    djtext = request.GET.get('text', 'default')
    analyzed=djtext
    mylist={}
    key1=("Reviews")
    passkey1=key1
    key2=("Ratings")
    passkey2=key2
    
    input_reviews = [analyzed]
    mylist.update({passkey1:analyzed})
    #print(mylist)
    #print("\nPredictions:")
    for review in input_reviews:
        print("\nReview:", review)
        probdist = classifier.prob_classify(extract_features(review.split()))
        pred_sentiment = probdist.max()
    #print("Predicted sentiment:", pred_sentiment)
    #print("Probability:", round(probdist.prob(pred_sentiment), 2))
    if  pred_sentiment=="Positive":
        if round(probdist.prob(pred_sentiment), 2)>=0.80:
            #print("Ratings calculated")
            rating=5.0
            mylist.update({passkey2:rating})
            
        elif round(probdist.prob(pred_sentiment), 2)>0.70 and round(probdist.prob(pred_sentiment), 2)<0.80:
            #print("Ratings calculated")
            rating=4.0
            mylist.update({passkey2:rating})
           
        elif round(probdist.prob(pred_sentiment), 2)>0.60 and round(probdist.prob(pred_sentiment), 2)<0.50:
            #print("Ratings calculated")
            rating=3.0
            mylist.update({passkey2:rating})
            
    elif pred_sentiment=="Negative":
        if round(probdist.prob(pred_sentiment), 2)>=0.80:
            #print("Ratings calculated")
            rating=1.0
            mylist.update({passkey2:rating})
            #print("*")
        elif round(probdist.prob(pred_sentiment), 2)<0.80:
            #print("Ratings calculated")
            rating=2.0
            mylist.update({passkey2:rating})
           # print("**")
    x=mycoll.insert_one(mylist)
    y=mycoll.aggregate([{"$group":{"_id":"null", "avgrating":{"$avg":"$Ratings"}}}])
    result=list(y)
    dekh={'id':result[0]['avgrating']}
    

    #return render(request,'check.html',dekh)

    params = {'mypred':pred_sentiment,'myreviews':analyzed,'myrating':mylist['Ratings'],'id':result[0]['avgrating']}
    return render(request,'analyze20.html',params)

def speaker(request):
    return render(request,'speaker.html')
def zebra(request):
    return render(request,'zebra.html')
def analyze21(request):
    mycoll=mydb["zebronics"]
    def extract_features(word_list):
        return dict([(word, True) for word in word_list])

    #if __name__ == "__main__":\\
    global positive_fileids,negative_fileids
    positive_fileids = movie_reviews.fileids("pos")
    negative_fileids = movie_reviews.fileids("neg")
    features_positive = [
        (extract_features(movie_reviews.words(fileids=[f])), "Positive")
        for f in positive_fileids
    ]
    features_negative = [
        (extract_features(movie_reviews.words(fileids=[f])), "Negative")
        for f in negative_fileids
    ]
    # Split the data into train and test (80/20)
    threshold_factor = 1.0
    threshold_positive = int(threshold_factor * len(features_positive))
    threshold_negative = int(threshold_factor * len(features_negative))
    features_train = (
        features_positive[:threshold_positive] + features_negative[:threshold_negative]
    )
    features_test = (
        features_positive[threshold_positive:] + features_negative[threshold_negative:]
    )
    #print("\nNumber of training datapoints:", len(features_train))
    #print("Number of test datapoints:", len(features_test))
    # Train a Naive Bayes classifier
    classifier = NaiveBayesClassifier.train(features_train)


    djtext = request.GET.get('text', 'default')
    analyzed=djtext
    mylist={}
    key1=("Reviews")
    passkey1=key1
    key2=("Ratings")
    passkey2=key2
    
    input_reviews = [analyzed]
    mylist.update({passkey1:analyzed})
    #print(mylist)
    #print("\nPredictions:")
    for review in input_reviews:
        print("\nReview:", review)
        probdist = classifier.prob_classify(extract_features(review.split()))
        pred_sentiment = probdist.max()
    #print("Predicted sentiment:", pred_sentiment)
    #print("Probability:", round(probdist.prob(pred_sentiment), 2))
    if  pred_sentiment=="Positive":
        if round(probdist.prob(pred_sentiment), 2)>=0.80:
            #print("Ratings calculated")
            rating=5.0
            mylist.update({passkey2:rating})
            
        elif round(probdist.prob(pred_sentiment), 2)>0.70 and round(probdist.prob(pred_sentiment), 2)<0.80:
            #print("Ratings calculated")
            rating=4.0
            mylist.update({passkey2:rating})
           
        elif round(probdist.prob(pred_sentiment), 2)>0.60 and round(probdist.prob(pred_sentiment), 2)<0.50:
            #print("Ratings calculated")
            rating=3.0
            mylist.update({passkey2:rating})
            
    elif pred_sentiment=="Negative":
        if round(probdist.prob(pred_sentiment), 2)>=0.80:
            #print("Ratings calculated")
            rating=1.0
            mylist.update({passkey2:rating})
            #print("*")
        elif round(probdist.prob(pred_sentiment), 2)<0.80:
            #print("Ratings calculated")
            rating=2.0
            mylist.update({passkey2:rating})
           # print("**")
    x=mycoll.insert_one(mylist)
    y=mycoll.aggregate([{"$group":{"_id":"null", "avgrating":{"$avg":"$Ratings"}}}])
    result=list(y)
    dekh={'id':result[0]['avgrating']}
    

    #return render(request,'check.html',dekh)

    params = {'mypred':pred_sentiment,'myreviews':analyzed,'myrating':mylist['Ratings'],'id':result[0]['avgrating']}
    return render(request,'analyze21.html',params)
def philips(request):
    return render(request,'philips.html')
def analyze22(request):
    mycoll=mydb["philips"]
    def extract_features(word_list):
        return dict([(word, True) for word in word_list])

    #if __name__ == "__main__":\\
    global positive_fileids,negative_fileids
    positive_fileids = movie_reviews.fileids("pos")
    negative_fileids = movie_reviews.fileids("neg")
    features_positive = [
        (extract_features(movie_reviews.words(fileids=[f])), "Positive")
        for f in positive_fileids
    ]
    features_negative = [
        (extract_features(movie_reviews.words(fileids=[f])), "Negative")
        for f in negative_fileids
    ]
    # Split the data into train and test (80/20)
    threshold_factor = 1.0
    threshold_positive = int(threshold_factor * len(features_positive))
    threshold_negative = int(threshold_factor * len(features_negative))
    features_train = (
        features_positive[:threshold_positive] + features_negative[:threshold_negative]
    )
    features_test = (
        features_positive[threshold_positive:] + features_negative[threshold_negative:]
    )
    #print("\nNumber of training datapoints:", len(features_train))
    #print("Number of test datapoints:", len(features_test))
    # Train a Naive Bayes classifier
    classifier = NaiveBayesClassifier.train(features_train)


    djtext = request.GET.get('text', 'default')
    analyzed=djtext
    mylist={}
    key1=("Reviews")
    passkey1=key1
    key2=("Ratings")
    passkey2=key2
    
    input_reviews = [analyzed]
    mylist.update({passkey1:analyzed})
    #print(mylist)
    #print("\nPredictions:")
    for review in input_reviews:
        print("\nReview:", review)
        probdist = classifier.prob_classify(extract_features(review.split()))
        pred_sentiment = probdist.max()
    #print("Predicted sentiment:", pred_sentiment)
    #print("Probability:", round(probdist.prob(pred_sentiment), 2))
    if  pred_sentiment=="Positive":
        if round(probdist.prob(pred_sentiment), 2)>=0.80:
            #print("Ratings calculated")
            rating=5.0
            mylist.update({passkey2:rating})
            
        elif round(probdist.prob(pred_sentiment), 2)>0.70 and round(probdist.prob(pred_sentiment), 2)<0.80:
            #print("Ratings calculated")
            rating=4.0
            mylist.update({passkey2:rating})
           
        elif round(probdist.prob(pred_sentiment), 2)>0.60 and round(probdist.prob(pred_sentiment), 2)<0.50:
            #print("Ratings calculated")
            rating=3.0
            mylist.update({passkey2:rating})
            
    elif pred_sentiment=="Negative":
        if round(probdist.prob(pred_sentiment), 2)>=0.80:
            #print("Ratings calculated")
            rating=1.0
            mylist.update({passkey2:rating})
            #print("*")
        elif round(probdist.prob(pred_sentiment), 2)<0.80:
            #print("Ratings calculated")
            rating=2.0
            mylist.update({passkey2:rating})
           # print("**")
    x=mycoll.insert_one(mylist)
    y=mycoll.aggregate([{"$group":{"_id":"null", "avgrating":{"$avg":"$Ratings"}}}])
    result=list(y)
    dekh={'id':result[0]['avgrating']}
    

    #return render(request,'check.html',dekh)

    params = {'mypred':pred_sentiment,'myreviews':analyzed,'myrating':mylist['Ratings'],'id':result[0]['avgrating']}
    return render(request,'analyze22.html',params)
def sonymusic(request):
    return render(request,'sonymusic.html')
def analyze23(request):
    mycoll=mydb["sonymusic"]
    def extract_features(word_list):
        return dict([(word, True) for word in word_list])

    #if __name__ == "__main__":\\
    global positive_fileids,negative_fileids
    positive_fileids = movie_reviews.fileids("pos")
    negative_fileids = movie_reviews.fileids("neg")
    features_positive = [
        (extract_features(movie_reviews.words(fileids=[f])), "Positive")
        for f in positive_fileids
    ]
    features_negative = [
        (extract_features(movie_reviews.words(fileids=[f])), "Negative")
        for f in negative_fileids
    ]
    # Split the data into train and test (80/20)
    threshold_factor = 1.0
    threshold_positive = int(threshold_factor * len(features_positive))
    threshold_negative = int(threshold_factor * len(features_negative))
    features_train = (
        features_positive[:threshold_positive] + features_negative[:threshold_negative]
    )
    features_test = (
        features_positive[threshold_positive:] + features_negative[threshold_negative:]
    )
    #print("\nNumber of training datapoints:", len(features_train))
    #print("Number of test datapoints:", len(features_test))
    # Train a Naive Bayes classifier
    classifier = NaiveBayesClassifier.train(features_train)


    djtext = request.GET.get('text', 'default')
    analyzed=djtext
    mylist={}
    key1=("Reviews")
    passkey1=key1
    key2=("Ratings")
    passkey2=key2
    
    input_reviews = [analyzed]
    mylist.update({passkey1:analyzed})
    #print(mylist)
    #print("\nPredictions:")
    for review in input_reviews:
        print("\nReview:", review)
        probdist = classifier.prob_classify(extract_features(review.split()))
        pred_sentiment = probdist.max()
    #print("Predicted sentiment:", pred_sentiment)
    #print("Probability:", round(probdist.prob(pred_sentiment), 2))
    if  pred_sentiment=="Positive":
        if round(probdist.prob(pred_sentiment), 2)>=0.80:
            #print("Ratings calculated")
            rating=5.0
            mylist.update({passkey2:rating})
            
        elif round(probdist.prob(pred_sentiment), 2)>0.70 and round(probdist.prob(pred_sentiment), 2)<0.80:
            #print("Ratings calculated")
            rating=4.0
            mylist.update({passkey2:rating})
           
        elif round(probdist.prob(pred_sentiment), 2)>0.60 and round(probdist.prob(pred_sentiment), 2)<0.50:
            #print("Ratings calculated")
            rating=3.0
            mylist.update({passkey2:rating})
            
    elif pred_sentiment=="Negative":
        if round(probdist.prob(pred_sentiment), 2)>=0.80:
            #print("Ratings calculated")
            rating=1.0
            mylist.update({passkey2:rating})
            #print("*")
        elif round(probdist.prob(pred_sentiment), 2)<0.80:
            #print("Ratings calculated")
            rating=2.0
            mylist.update({passkey2:rating})
           # print("**")
    x=mycoll.insert_one(mylist)
    y=mycoll.aggregate([{"$group":{"_id":"null", "avgrating":{"$avg":"$Ratings"}}}])
    result=list(y)
    dekh={'id':result[0]['avgrating']}
    

    #return render(request,'check.html',dekh)

    params = {'mypred':pred_sentiment,'myreviews':analyzed,'myrating':mylist['Ratings'],'id':result[0]['avgrating']}
    return render(request,'analyze23.html',params)
def saregama(request):
    return render(request,'saregama.html')
def analyze24(request):
    mycoll=mydb["saregama"]
    def extract_features(word_list):
        return dict([(word, True) for word in word_list])

    #if __name__ == "__main__":\\
    global positive_fileids,negative_fileids
    positive_fileids = movie_reviews.fileids("pos")
    negative_fileids = movie_reviews.fileids("neg")
    features_positive = [
        (extract_features(movie_reviews.words(fileids=[f])), "Positive")
        for f in positive_fileids
    ]
    features_negative = [
        (extract_features(movie_reviews.words(fileids=[f])), "Negative")
        for f in negative_fileids
    ]
    # Split the data into train and test (80/20)
    threshold_factor = 1.0
    threshold_positive = int(threshold_factor * len(features_positive))
    threshold_negative = int(threshold_factor * len(features_negative))
    features_train = (
        features_positive[:threshold_positive] + features_negative[:threshold_negative]
    )
    features_test = (
        features_positive[threshold_positive:] + features_negative[threshold_negative:]
    )
    #print("\nNumber of training datapoints:", len(features_train))
    #print("Number of test datapoints:", len(features_test))
    # Train a Naive Bayes classifier
    classifier = NaiveBayesClassifier.train(features_train)


    djtext = request.GET.get('text', 'default')
    analyzed=djtext
    mylist={}
    key1=("Reviews")
    passkey1=key1
    key2=("Ratings")
    passkey2=key2
    
    input_reviews = [analyzed]
    mylist.update({passkey1:analyzed})
    #print(mylist)
    #print("\nPredictions:")
    for review in input_reviews:
        print("\nReview:", review)
        probdist = classifier.prob_classify(extract_features(review.split()))
        pred_sentiment = probdist.max()
    #print("Predicted sentiment:", pred_sentiment)
    #print("Probability:", round(probdist.prob(pred_sentiment), 2))
    if  pred_sentiment=="Positive":
        if round(probdist.prob(pred_sentiment), 2)>=0.80:
            #print("Ratings calculated")
            rating=5.0
            mylist.update({passkey2:rating})
            
        elif round(probdist.prob(pred_sentiment), 2)>0.70 and round(probdist.prob(pred_sentiment), 2)<0.80:
            #print("Ratings calculated")
            rating=4.0
            mylist.update({passkey2:rating})
           
        elif round(probdist.prob(pred_sentiment), 2)>0.60 and round(probdist.prob(pred_sentiment), 2)<0.50:
            #print("Ratings calculated")
            rating=3.0
            mylist.update({passkey2:rating})
            
    elif pred_sentiment=="Negative":
        if round(probdist.prob(pred_sentiment), 2)>=0.80:
            #print("Ratings calculated")
            rating=1.0
            mylist.update({passkey2:rating})
            #print("*")
        elif round(probdist.prob(pred_sentiment), 2)<0.80:
            #print("Ratings calculated")
            rating=2.0
            mylist.update({passkey2:rating})
           # print("**")
    x=mycoll.insert_one(mylist)
    y=mycoll.aggregate([{"$group":{"_id":"null", "avgrating":{"$avg":"$Ratings"}}}])
    result=list(y)
    dekh={'id':result[0]['avgrating']}
    

    #return render(request,'check.html',dekh)

    params = {'mypred':pred_sentiment,'myreviews':analyzed,'myrating':mylist['Ratings'],'id':result[0]['avgrating']}
    return render(request,'analyze24.html',params)
def boatmusic(request):
    return render(request,'boatmusic.html')
def analyze25(request):
    mycoll=mydb["boatstone"]
    def extract_features(word_list):
        return dict([(word, True) for word in word_list])

    #if __name__ == "__main__":\\
    global positive_fileids,negative_fileids
    positive_fileids = movie_reviews.fileids("pos")
    negative_fileids = movie_reviews.fileids("neg")
    features_positive = [
        (extract_features(movie_reviews.words(fileids=[f])), "Positive")
        for f in positive_fileids
    ]
    features_negative = [
        (extract_features(movie_reviews.words(fileids=[f])), "Negative")
        for f in negative_fileids
    ]
    # Split the data into train and test (80/20)
    threshold_factor = 1.0
    threshold_positive = int(threshold_factor * len(features_positive))
    threshold_negative = int(threshold_factor * len(features_negative))
    features_train = (
        features_positive[:threshold_positive] + features_negative[:threshold_negative]
    )
    features_test = (
        features_positive[threshold_positive:] + features_negative[threshold_negative:]
    )
    #print("\nNumber of training datapoints:", len(features_train))
    #print("Number of test datapoints:", len(features_test))
    # Train a Naive Bayes classifier
    classifier = NaiveBayesClassifier.train(features_train)


    djtext = request.GET.get('text', 'default')
    analyzed=djtext
    mylist={}
    key1=("Reviews")
    passkey1=key1
    key2=("Ratings")
    passkey2=key2
    
    input_reviews = [analyzed]
    mylist.update({passkey1:analyzed})
    #print(mylist)
    #print("\nPredictions:")
    for review in input_reviews:
        print("\nReview:", review)
        probdist = classifier.prob_classify(extract_features(review.split()))
        pred_sentiment = probdist.max()
    #print("Predicted sentiment:", pred_sentiment)
    #print("Probability:", round(probdist.prob(pred_sentiment), 2))
    if  pred_sentiment=="Positive":
        if round(probdist.prob(pred_sentiment), 2)>=0.80:
            #print("Ratings calculated")
            rating=5.0
            mylist.update({passkey2:rating})
            
        elif round(probdist.prob(pred_sentiment), 2)>0.70 and round(probdist.prob(pred_sentiment), 2)<0.80:
            #print("Ratings calculated")
            rating=4.0
            mylist.update({passkey2:rating})
           
        elif round(probdist.prob(pred_sentiment), 2)>0.60 and round(probdist.prob(pred_sentiment), 2)<0.50:
            #print("Ratings calculated")
            rating=3.0
            mylist.update({passkey2:rating})
            
    elif pred_sentiment=="Negative":
        if round(probdist.prob(pred_sentiment), 2)>=0.80:
            #print("Ratings calculated")
            rating=1.0
            mylist.update({passkey2:rating})
            #print("*")
        elif round(probdist.prob(pred_sentiment), 2)<0.80:
            #print("Ratings calculated")
            rating=2.0
            mylist.update({passkey2:rating})
           # print("**")
    x=mycoll.insert_one(mylist)
    y=mycoll.aggregate([{"$group":{"_id":"null", "avgrating":{"$avg":"$Ratings"}}}])
    result=list(y)
    dekh={'id':result[0]['avgrating']}
    

    #return render(request,'check.html',dekh)

    params = {'mypred':pred_sentiment,'myreviews':analyzed,'myrating':mylist['Ratings'],'id':result[0]['avgrating']}
    return render(request,'analyze25.html',params)