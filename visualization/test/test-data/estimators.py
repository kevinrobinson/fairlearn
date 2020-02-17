import json

def parsed(line):
  fields = []
  for field in line.split(','):
    fields.append(field.strip())
  return fields

def process():
  with open('./uci-adult.data') as file:
    records = []
    for line in file:
      fields = parsed(line)
      records.append(fields)

    return records

records = process()
print('records: {}'.format(len(records)))
print(records[0:2])



# from sklearn.feature_extraction import DictVectorizer
# from sklearn.feature_selection import SelectKBest, chi2
# X =
# y = 
# clf = LogisticRegression(random_state=0).fit(X, y)
# clf.predict(X[:2, :])

# v = DictVectorizer(sparse=False)
# X = v.fit_transform(records)
# print(X[0:3])
# print(v.get_feature_names())
# print(len(v.get_feature_names()))

# D = [{'foo': 1, 'bar': 2}, {'foo': 3, 'baz': 1}]
# X = v.fit_transform(D)
# print(D)
# print(X)
# support = SelectKBest(chi2, k=2).fit(X, [0, 1])
# print(v.get_feature_names())

features = [
  'age',
  'workclass',
  'fnlwgt',
  'education',
  'education-num',
  'marital-status',
  'occupation',
  'relationship',
  'race',
  'sex',
  'capital-gain',
  'capital-loss',
  'hours-per-week',
  'native-country',
  'income-label'
]


# from sklearn.preprocessing import OrdinalEncoder
# enc = OrdinalEncoder()
# print(enc.fit(X))
# print(enc.categories_)

# preprocessing

# import numpy as np
# X_scaled = preprocessing.scale(X)

# X
narrow_records = [[record[3], record[6]] for record in records]
from sklearn.preprocessing import OneHotEncoder
x_encoder = OneHotEncoder()
x_encoder.fit(narrow_records)
X_encoded = x_encoder.transform(narrow_records)
print('x categories: {}'.format(x_encoder.categories_))
# print(X_encoded)

# y
# from sklearn.preprocessing import LabelBinarizer
# labels = [record[-1] for record in records]
# lb = LabelBinarizer(pos_label='>50K')
# print(lb.fit(labels))
y_encoded = [1 if record[-1] == '>50K' else 0 for record in records]
# print(y_encoded)

print('x:')
print(X_encoded[0:2])
print('y:')
print(y_encoded[0:2])
from sklearn.linear_model import LogisticRegression
clf = LogisticRegression(random_state=0).fit(X_encoded, y_encoded)
print(clf)
clf.predict(X_encoded[:2, :])

