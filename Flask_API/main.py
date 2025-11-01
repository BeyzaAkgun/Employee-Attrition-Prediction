import fileinput
import os
from io import BytesIO

import flask
import openpyxl
from flask_cors import CORS, cross_origin
from flask import jsonify, request, Flask, send_file, redirect, url_for, send_from_directory
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns;
from openpyxl.reader.excel import load_workbook
from werkzeug.utils import secure_filename

app = Flask(__name__)

api_cors_config = {
    "origins": ["http://localhost:5173"],
    "methods": ["GET", "POST"],
    "allow_headers": ["*"]
}
# cors=CORS(app, resources=api_cors_config)
# \\Users\\kubil
UPLOAD_FOLDER = 'C:\\Desktop\\'
ALLOWED_EXTENSIONS = {'csv'}
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

sns.set()
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.feature_selection import SelectFromModel
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.metrics import f1_score, precision_score, recall_score
from sklearn.ensemble import AdaBoostClassifier
stat = 0
employee_data = pd.read_csv('C:\\Users\\kubil\\Desktop\\predict_employee_attrition.csv')
print(employee_data)
# To read the file and see the dataset
employee_data = employee_data.drop(columns=['Over18', 'EmployeeCount', 'StandardHours'])
print(employee_data.head())
print(employee_data.info())
print(employee_data.describe())

data = zip(employee_data['Age'], employee_data['DailyRate'], employee_data['DistanceFromHome'],
           employee_data['Education'], employee_data['EnvironmentSatisfaction'], employee_data['JobLevel'],
           employee_data['YearsSinceLastPromotion'], employee_data['WorkLifeBalance'],
           employee_data['RelationshipSatisfaction'])
syn_data = pd.DataFrame(data, columns=['Age', 'DailyRate', 'DistanceFromHome', 'Education', 'EnvironmentSatisfaction',
                                       'JobLevel', 'YearsSinceLastPromotion', 'WorkLifeBalance',
                                       'RelationshipSatisfaction'])
print(syn_data.head())

plt.scatter(employee_data['Age'], employee_data['Attrition'])
# plt.show()

plt.plot(employee_data['Age'], employee_data['Attrition'])
# plt.show()

see = zip(employee_data['JobLevel'])
syn = pd.DataFrame(see, columns=['JobLevel'])
print(syn)

encoding_map = {'Attrition': {'Yes': 1, 'No': 0},
                'BusinessTravel': {'Non-Travel': 0, 'Travel_Rarely': 1, 'Travel_Frequently': 2},
                'Department': {'Sales': 0, 'Research & Development': 1, 'Human Resources': 2},
                'EducationField': {'Other': 0, 'Life Sciences': 1, 'Medical': 2, 'Marketing': 3, 'Technical Degree': 4,
                                   'Human Resources': 5},
                'Gender': {'Female': 0, 'Male': 1},
                'JobRole': {'Sales Executive': 0, 'Research Scientist': 1, 'Laboratory Technician': 2,
                            'Manufacturing Director': 3, 'Healthcare Representative': 4, 'Manager': 5,
                            'Sales Representative': 6, 'Research Director': 7, 'Human Resources': 8},
                'MaritalStatus': {'Single': 0, 'Married': 1, 'Divorced': 2}, 'OverTime': {'Yes': 1, 'No': 0}}

employee_data.replace(encoding_map, inplace=True)
employee_data.drop_duplicates(inplace=True)
print(employee_data)
print(employee_data.info())

features = ['Age', 'BusinessTravel', 'DailyRate', 'Department', 'DistanceFromHome', 'Education', 'EducationField',
            'EmployeeNumber', 'EnvironmentSatisfaction', 'Gender', 'HourlyRate', 'JobInvolvement', 'JobLevel',
            'JobRole', 'JobSatisfaction', 'MaritalStatus', 'MonthlyIncome', 'MonthlyRate', 'NumCompaniesWorked',
            'OverTime', 'PercentSalaryHike', 'PerformanceRating', 'RelationshipSatisfaction', 'StockOptionLevel',
            'TotalWorkingYears', 'TrainingTimesLastYear', 'WorkLifeBalance', 'YearsAtCompany', 'YearsInCurrentRole',
            'YearsSinceLastPromotion', 'YearsWithCurrManager']
target = ['Attrition']
X = np.array(employee_data[features].values)
y = np.array(employee_data[target].values).ravel()
# Normalization
minX = X.min(axis=0)
maxX = X.max(axis=0)
X = (X - minX) / (maxX - minX)
print("Normalization: ", X[:10])

# Selecting manually
feature_selection = SelectKBest(chi2, k=5)
feature_selection.fit(X, y)

transformedX = feature_selection.transform(X)
print(f"Old Shape: {X.shape} New shape: {transformedX.shape}")
print('\t'.join(features))
print('\t '.join([f"{s:.5f}" for s in feature_selection.scores_]))
print('\t '.join([f"{p:.7f}" for p in feature_selection.pvalues_]))

# Auto selecting
feature_selection = SelectFromModel(LogisticRegression(tol=1e-1))
feature_selection.fit(X, y)

transformedX = feature_selection.transform(X)
print(f"New shape: {transformedX.shape}")
print("Selected features: ", feature_selection.get_support())
print("Selected features: ", np.array(features)[feature_selection.get_support(indices=True)])

feature_selection = SelectFromModel(LinearSVC(tol=1e-1))
feature_selection.fit(X, y)

transformedX = feature_selection.transform(X)
print(f"New shape: {transformedX.shape}")
print("Selected features: ", feature_selection.get_support())
print("Selected features: ", np.array(features)[feature_selection.get_support(indices=True)])

feature_selection = SelectFromModel(DecisionTreeClassifier())
feature_selection.fit(X, y)

transformedX = feature_selection.transform(X)
print(f"New shape: {transformedX.shape}")

print("Selected features: ", feature_selection.get_support())
print("Selected features: ", np.array(features)[feature_selection.get_support(indices=True)])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=20)  # 60% train, %40 test

X_valid, X_test, y_valid, y_test = train_test_split(X_test, y_test, test_size=0.5, random_state=15)  # 50% val, 50% test
print(f'Total # of sample in whole dataset: {len(X)}')
print(f'Total # of sample in train dataset: {len(X_train)}')
print(f'Total # of sample in validation dataset: {len(X_valid)}')
print(f'Total # of sample in test dataset: {len(X_test)}')

# logistic regression
# f_model = AdaBoostClassifier()
# f_model = LogisticRegression(C=2.7, penalty='l2', solver='liblinear')
f_model = AdaBoostClassifier(n_estimators=40, learning_rate=1.0)
f_model.fit(X_train, y_train)

validation_score = f_model.score(X_valid, y_valid)
print(f'Validation score of trained model: {validation_score}')

test_score = f_model.score(X_test, y_test)
print(f'Test score of trained model: {test_score}')

# Confusion Matrix
y_predictions = f_model.predict(X_test)  # Predicting from the test data
print(y_predictions)
conf_matrix = confusion_matrix(y_test, y_predictions)
print(f'Accuracy: {accuracy_score(y_test, y_predictions)}')
print(f'Confussion matrix: \n{conf_matrix}\n')
print(f'F1 score : {f1_score(y_test, y_predictions)}')
print(f'precision score : {precision_score(y_test, y_predictions)}')
print(f'recall score : {recall_score(y_test, y_predictions)}')

person = np.array(
    [41, 1, 1102, 0, 1, 2, 1, 1, 2, 0, 94, 3, 2, 0, 4, 0, 5993, 19479, 8, 1, 11, 3, 1, 0, 8, 0, 1, 6, 4, 0, 5])
person = person.reshape(1, -1)
person = (person - minX) / (maxX - minX)
apredict = f_model.predict(person)
print(apredict)


def predict_attrition(Name, Surname, Age, BusinessTravel, DailyRate, Department, DistanceFromHome, Education,
                      EducationField,
                      EmployeeNumber, EnvironmentSatisfaction, Gender, HourlyRate, JobInvolvement,
                      JobLevel, JobRole, JobSatisfaction, MaritalStatus, MonthlyIncome, MonthlyRate,
                      NumCompaniesWorked, OverTime, PercentSalaryHike, PerformanceRating, RelationshipSatisfaction,
                      StockOptionLevel, TotalWorkingYears, TrainingTimesLastYear, WorkLifeBalance, YearsAtCompany,
                      YearsInCurrentRole, YearsSinceLastPromotion, YearsWithCurrManager):
    if BusinessTravel == 'Non-Travel':
        BusinessTravel = 0
    elif BusinessTravel == 'Travel_Rarely':
        BusinessTravel = 1
    elif BusinessTravel == 'Travel_Frequently':
        BusinessTravel = 2

    if Department == 'Sales':
        Department = 0
    elif Department == 'Research & Development':
        Department = 1
    elif Department == 'Human Resources':
        Department = 2

    if EducationField == 'Other':
        EducationField = 0
    elif EducationField == 'Life Sciences':
        EducationField = 1
    elif EducationField == 'Medical':
        EducationField = 2
    elif EducationField == 'Marketing':
        EducationField = 3
    elif EducationField == 'Technical Degree':
        EducationField = 4
    elif EducationField == 'Human Resources':
        EducationField = 5

    if Gender == 'Female':
        Gender = 0
    elif Gender == 'Male':
        Gender = 1

    if JobRole == 'Sales Executive':
        JobRole = 0
    elif JobRole == 'Research Scientist':
        JobRole = 1
    elif JobRole == 'Laboratory Technician':
        JobRole = 2
    elif JobRole == 'Manufacturing Director':
        JobRole = 3
    elif JobRole == 'Healthcare Representative':
        JobRole = 4
    elif JobRole == 'Manager':
        JobRole = 5
    elif JobRole == 'Sales Representative':
        JobRole = 6
    elif JobRole == 'Research Director':
        JobRole = 7
    elif JobRole == 'Human Resources':
        JobRole = 8

    if MaritalStatus == 'Single':
        MaritalStatus = 0
    elif MaritalStatus == 'Married':
        MaritalStatus = 1
    elif MaritalStatus == 'Divorced':
        MaritalStatus = 2

    if OverTime == 'Yes':
        OverTime = 1
    elif OverTime == 'No':
        OverTime = 0

    employee = np.array([Age, BusinessTravel, DailyRate, Department, DistanceFromHome, Education, EducationField,
                         EmployeeNumber, EnvironmentSatisfaction, Gender, HourlyRate, JobInvolvement,
                         JobLevel, JobRole, JobSatisfaction, MaritalStatus, MonthlyIncome, MonthlyRate,
                         NumCompaniesWorked, OverTime, PercentSalaryHike, PerformanceRating, RelationshipSatisfaction,
                         StockOptionLevel, TotalWorkingYears, TrainingTimesLastYear, WorkLifeBalance, YearsAtCompany,
                         YearsInCurrentRole, YearsSinceLastPromotion, YearsWithCurrManager])
    employee = employee.reshape(1, -1)
    employee = (employee - minX) / (maxX - minX)
    predict_employee_attrition = f_model.predict(employee)
    predict_employee_attrition_str = 'Very Likely' if predict_employee_attrition == 1 else 'No'
    return f'{Name} {Surname} : {predict_employee_attrition_str}'


result = predict_attrition('Kubilay', 'Kürtür', 37, 'Travel_Rarely', 1373, 'Research & Development', 2, 2, 'Other', 4,
                           4, 'Male', 92, 2, 1, 'Laboratory Technician', 3, 'Single', 2090, 2396, 6, 'Yes', 15, 3, 2, 0,
                           7, 3, 3, 0, 0, 0, 0)
print(result)
result2 = predict_attrition('Kubilay', 'Kürtür', 49, 'Travel_Frequently', 279, 'Research & Development', 8, 1,
                            'Life Sciences', 2, 3, 'Male', 61, 2, 2, 'Research Scientist', 2, 'Married', 5130, 24907, 1,
                            'No', 23, 4, 4, 1, 10, 3, 3, 10, 7, 1, 7)
print(result2)
result3 = predict_attrition('Kubilay', 'Kürtür', 33, 'Travel_Frequently', 1392, 'Research & Development', 3, 4,
                            'Life Sciences', 5, 4, 'Female', 56, 3, 1, 'Research Scientist', 3, 'Married', 2909, 23159,
                            1, 'Yes', 11, 3, 3, 0, 8, 3, 3, 8, 7, 3, 0)
print(result3)
result4 = predict_attrition('Kubilay', 'Kürtür', 28, 'Travel_Rarely', 103, 'Research & Development', 24, 3,
                            'Life Sciences', 19, 3, 'Male', 50, 2, 1, 'Laboratory Technician', 3, 'Single', 2028, 12947,
                            5, 'Yes', 14, 3, 2, 0, 6, 4, 3, 4, 2, 0, 3)
print(result4)
result5 = predict_attrition('Kubilay', 'Kürtür', 41, 'Travel_Rarely', 1102, 'Sales', 1, 2, 'Life Sciences', 1, 2,
                            'Female', 94, 3, 2, 'Sales Executive', 4, 'Single', 5993, 19479, 8, 'Yes', 11, 3, 1, 0, 8,
                            0, 1, 6, 4, 0, 5)
print(result5)


# @app.route('/upload', methods=['POST'])
def predict_attrition_csv(csv_file) -> flask.Response:
    encoding_map = {'BusinessTravel': {'Non-Travel': 0, 'Travel_Rarely': 1, 'Travel_Frequently': 2},
                    'Department': {'Sales': 0, 'Research & Development': 1, 'Human Resources': 2},
                    'EducationField': {'Other': 0, 'Life Sciences': 1, 'Medical': 2, 'Marketing': 3,
                                       'Technical Degree': 4, 'Human Resources': 5},
                    'Gender': {'Female': 0, 'Male': 1},
                    'JobRole': {'Sales Executive': 0, 'Research Scientist': 1, 'Laboratory Technician': 2,
                                'Manufacturing Director': 3, 'Healthcare Representative': 4, 'Manager': 5,
                                'Sales Representative': 6, 'Research Director': 7, 'Human Resources': 8},
                    'MaritalStatus': {'Single': 0, 'Married': 1, 'Divorced': 2}, 'OverTime': {'Yes': 1, 'No': 0}}

    decoding_map = {'BusinessTravel': {0: 'Non-Travel', 1: 'Travel_Rarely', 2: 'Travel_Frequently'},
                    'Department': {0: 'Sales', 1: 'Research & Development', 2: 'Human Resources'},
                    'EducationField': {0: 'Other', 1: 'Life Sciences', 2: 'Medical', 3: 'Marketing',
                                       4: 'Technical Degree', 5: 'Human Resources'},
                    'Gender': {0: 'Female', 1: 'Male'},
                    'JobRole': {0: 'Sales Executive', 1: 'Research Scientist', 2: 'Laboratory Technician',
                                3: 'Manufacturing Director', 4: 'Healthcare Representative', 5: 'Manager',
                                6: 'Sales Representative', 7: 'Research Director', 8: 'Human Resources'},
                    'MaritalStatus': {0: 'Single', 1: 'Married', 2: 'Divorced'}, 'OverTime': {1: 'Yes', 0: 'No'}}
    emp_data = pd.read_csv(csv_file)

    emp_data.replace(encoding_map, inplace=True)

    names = emp_data['Name']
    surnames = emp_data['Surname']

    emp_data = emp_data.drop(columns=['Name', 'Surname'])
    valuess = np.array(emp_data.values)
    valuess = (valuess - minX) / (maxX - minX)
    preds = f_model.predict(valuess)

    counter = 0
    for i in preds:
        if i == 1:
            counter += 1

    statistics = (counter / preds.size) * 100
    global stat
    stat = statistics
    # preds=preds.reshape(12,1)
    emp_data['Attrition'] = preds
    emp_data['Name'] = names
    emp_data['Surname'] = surnames
    emp_data['%_Attrition'] = None
    emp_data.loc[0, '%_Attrition'] = statistics
    emp_data.replace(decoding_map, inplace=True)
    # emp_data, statistics,
    file_path = 'predFileC.csv'  # Specify the file path where you want to save the file
    emp_data.to_csv(file_path)
    return send_file(
        file_path,
        as_attachment=True,
        mimetype='text/csv',
        download_name='predFileC.csv'
    )


@app.route('/upload/csv', methods=['POST'])
@cross_origin(origins=["http://localhost:5173"])
def upload_file_csv():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # result = predict_attrition_csv(file_path)

        # Delete the uploaded file after processing (optional)
        # os.remove(file_path)

        return predict_attrition_csv(file_path)


@app.route('/upload/excel', methods=['POST', 'OPTIONS'])
@cross_origin(origins=["http://localhost:5173"])
def upload_file_excel():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        # Delete the uploaded file after processing (optional)
        # os.remove(file_path)
        # predict_attrition_excel(file_path)
        # return send_file('predFileE.xlsx', as_attachment=True)
        return predict_attrition_excel(file_path)


def predict_attrition_excel(excel_file) -> flask.Response:
    encoding_map = {'Business Travel': {'Non-Travel': 0, 'Rarely': 1, 'Frequently': 2},
                    'Education': {'College': 2, 'Below College': 1, 'Bachelor': 3, 'Master': 4, 'Doctor': 5},
                    'Environment Satisfaction': {'Low': 1, 'Medium': 2, 'High': 3, 'Very High': 4},
                    'Job Involvement': {'Low': 1, 'Medium': 2, 'High': 3, 'Very High': 4},
                    'Relationship Satisfaction': {'Low': 1, 'Medium': 2, 'High': 3, 'Very High': 4},
                    'Job Satisfaction': {'Low': 1, 'Medium': 2, 'High': 3, 'Very High': 4},
                    'Performance Rating': {'Low': 1, 'Good': 2, 'Excellent': 3, 'Outstanding': 4},
                    'Work Life Balance': {'Bad': 1, 'Good': 2, 'Better': 3, 'Best': 4},
                    'Department': {'Sales': 0, 'Research & Development': 1, 'Human Resources': 2},
                    'Education Field': {'Other': 0, 'Life Sciences': 1, 'Medical': 2, 'Marketing': 3,
                                        'Technical Degree': 4, 'Human Resources': 5},
                    'Gender': {'Female': 0, 'Male': 1},
                    'Job Role': {'Sales Executive': 0, 'Research Scientist': 1, 'Laboratory Technician': 2,
                                 'Manufacturing Director': 3, 'Healthcare Representative': 4, 'Manager': 5,
                                 'Sales Representative': 6, 'Research Director': 7, 'Human Resources': 8},
                    'Marital Status': {'Single': 0, 'Married': 1, 'Divorced': 2}, 'Over Time': {'Yes': 1, 'No': 0}}
    decoding_map = {'BusinessTravel': {0: 'Non-Travel', 1: 'Travel_Rarely', 2: 'Travel_Frequently'},
                    'Department': {0: 'Sales', 1: 'Research & Development', 2: 'Human Resources'},
                    'EducationField': {0: 'Other', 1: 'Life Sciences', 2: 'Medical', 3: 'Marketing',
                                       4: 'Technical Degree', 5: 'Human Resources'},
                    'Gender': {0: 'Female', 1: 'Male'},
                    'JobRole': {0: 'Sales Executive', 1: 'Research Scientist', 2: 'Laboratory Technician',
                                3: 'Manufacturing Director', 4: 'Healthcare Representative', 5: 'Manager',
                                6: 'Sales Representative', 7: 'Research Director', 8: 'Human Resources'},
                    'MaritalStatus': {0: 'Single', 1: 'Married', 2: 'Divorced'}, 'OverTime': {1: 'Yes', 0: 'No'}}
    emps_data = pd.read_excel(excel_file, engine='openpyxl')
    emps_data.replace(encoding_map, inplace=True)
    namess = emps_data['Name']
    surnamess = emps_data['Surname']
    emps_data = emps_data.drop(columns=['Name', 'Surname'])

    valuess = np.array(emps_data.values)

    valuess = (valuess - minX) / (maxX - minX)

    predss = f_model.predict(valuess)

    counter = 0
    for i in predss:
        if i == 1:
            counter += 1

    statistics = (counter / predss.size) * 100
    global stat
    stat = statistics
    emps_data['Attrition'] = predss
    emps_data['Name'] = namess
    emps_data['Surname'] = surnamess
    emps_data['%_Attrition'] = None
    emps_data.loc[0, '%_Attrition'] = statistics
    emps_data.replace(decoding_map, inplace=True)
    # file_excel = emps_data.to_excel('predFileE.xlsx', engine='openpyxl')
    # return file_excel

    output = BytesIO()
    # writer = pd.ExcelWriter(output, engine='openpyxl')

    emps_data.to_excel(output, engine="openpyxl")
    # writer.book.save(output)
    output.seek(0)
    
    response = flask.make_response(
        output.getvalue()
    )
    response.headers.update({
        "Content-Type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        "Content-Disposition": "attachment; filename=predFileE.xlsx",
    })
    return response

@app.route('/statistics', methods=['GET'])
@cross_origin(origins=["http://localhost:5173"])
def give_stat():
    return jsonify(stat)


# file = 'C:\\Users\\kubil\\Desktop\\example.csv'
# print(predict_attrition_csv(file))

# excelFile = 'Desktop\ListExample.xlsx'
# print(predict_attrition_excel(excelFile))

if __name__ == "__main__":
    app.run(debug=True)
