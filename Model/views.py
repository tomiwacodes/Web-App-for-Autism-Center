from django.shortcuts import render
from joblib import load
model = load('./savedModels/model.joblib')

def predictor(request):
    if request.method == 'POST':
        Question9 = request.POST['Question9']
        Question7 = request.POST['Question7']
        Question2 = request.POST['Question2']
        Question8 = request.POST['Question8']
        Question3 = request.POST['Question3']
        Question5 = request.POST['Question5']
        Question6 = request.POST['Question6']
        Question1 = request.POST['Question1']
        Age_in_months = request.POST['Age_in_months']
        Question10 = request.POST['Question10']
        Question4 = request.POST['Question4']
        Jaundice = request.POST['Jaundice']
        Asian = request.POST['Asian']
        Family_Member = request.POST['Family_Member']
        Latino = request.POST['Latino']
        Middle_Eastern = request.POST['Middle_Eastern']
        Sex = request.POST['Sex']
        SouthAsian = request.POST['SouthAsian']
        Hispanic = request.POST['Hispanic']
        Family = request.POST['Family']

        list = [Question1, Question10, Question2, Question3, Question4, Question5, Question6, Question7, Question8, Question9]
        if ((Question9 == 'Sometimes')or(Question9=='Never')or(Question9=='Rarely')):
            Question9 = 1
        else:
            Question9 = 0
        
        if ((Question1 == 'Sometimes')or(Question1=='Never')or(Question1=='Rarely')):
            Question1 = 1
        else:
            Question1 = 0

        if ((Question2 == 'Sometimes')or(Question2=='Never')or(Question2=='Rarely')):
            Question2 = 1
        else:
            Question2 = 0

        if ((Question3 == 'Sometimes')or(Question3=='Never')or(Question3=='Rarely')):
            Question3 = 1
        else:
            Question3 = 0
        
        if ((Question4 == 'Sometimes')or(Question4=='Never')or(Question4=='Rarely')):
            Question4 = 1
        else:
            Question4 = 0
        
        if ((Question5 == 'Sometimes')or(Question5=='Never')or(Question5=='Rarely')):
            Question5 = 1
        else:
            Question5 = 0

        if ((Question6 == 'Sometimes')or(Question6=='Never')or(Question6=='Rarely')):
            Question6 = 1
        else:
            Question6 = 0
        
        if ((Question7 == 'Sometimes')or(Question7=='Never')or(Question7=='Rarely')):
            Question7 = 1
        else:
            Question7 = 0

        if ((Question8 == 'Sometimes')or(Question8=='Never')or(Question8=='Rarely')):
            Question8 = 1
        else:
            Question8 = 0
        
        if ((Question10 == 'Sometimes')or(Question10=='Never')or(Question10=='Rarely')):
            Question10 = 1
        else:
            Question10 = 0

        if((Jaundice=='Yes')or(Jaundice=='yes')or(Jaundice=='Y')or(Jaundice=='y')):
            Jaundice = 1
        else:
            Jaundice = 0
        
        if((Asian=='Yes')or(Asian=='yes')or(Asian=='Y')or(Asian=='y')):
            Asian = 1
        else:
            Asian = 0

        if((Family=='Yes')or(Family=='yes')or(Family=='Y')or(Family=='y')):
            Family = 1
        else:
            Family = 0

        if((Family_Member=='Yes')or(Family_Member=='yes')or(Family_Member=='Y')or(Family_Member=='y')):
            Family_Member = 1
        else:
            Family_Member = 0
        
        if((Latino=='Yes')or(Latino=='yes')or(Latino=='Y')or(Latino=='y')):
            Latino = 1
        else:
            Latino = 0
        
        if((Middle_Eastern=='Yes')or(Middle_Eastern=='yes')or(Middle_Eastern=='Y')or(Middle_Eastern=='y')):
            Middle_Eastern = 1
        else:
            Middle_Eastern = 0

        if((Sex=='Yes')or(Sex=='yes')or(Sex=='Y')or(Sex=='y')):
            Sex = 1
        else:
            Sex = 0

        if((SouthAsian=='Yes')or(SouthAsian=='yes')or(SouthAsian=='Y')or(SouthAsian=='y')):
            SouthAsian = 1
        else:
            SouthAsian = 0

        if((Hispanic=='Yes')or(Hispanic=='yes')or(Hispanic=='Y')or(Hispanic=='y')):
            Hispanic = 1
        else:
            Hispanic = 0
        
        y_pred = model.predict([[int(Question9), int(Question7), int(Question2), int(Question8), int(Question3), int(Question5), int(Question6), int(Question1), int(Age_in_months), int(Question10), int(Question4), int(Jaundice), int(Asian), int(Family_Member), int(Latino), int(Middle_Eastern), int(Sex), int(SouthAsian), int(Hispanic), int(Family)]])
        if(y_pred[0] == 1):
            y_pred = 'The patient is at risk for Autism'
        else:
            y_pred = 'The patient is not likely at risk of Autism'
        return render(request, 'main.html', {'result' : y_pred})
    return render(request, 'main.html')

