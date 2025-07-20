# IMDB-sentiment-classifier-using-TF-IDF-Machine-learning-using-Python
#### Date:Apr13 -2025
This project focuses on  Imdb movie reviews using NLP.
- **Dataset collection:**
Loaded "imdb" dataset from huggingface, it containing movie reviews text with sentiment labels `0-Negative`,`1-Positive`.

- **Text Preprocessing:**
Extract review texts and used nltk for cleaning.
Nltk source to download it stopwords,wordnet,omw for lemmatization.
Cleaned texts apply in new column.

- **Data split:**
split dataset into  train and validation sets.

- **Features extraction:**
Clean words used tfidf to convert into numerical features.

- **Model trainning:**
using classification algorithms logistic regression,naive bayes(multinomalNB) to train a models.
- **Evaluation:**
validation accuracy,test accuracy for the model performance and comparision.
Also did classification report `precision FP,recall FN,f1 score`.
Logistic regression achieve the `validation accuracy 88% `and `test accuracy 87%`.
Logistic regression classifier high precision,recall ,f1 score fewer of FP,FN then perform well.

- **Final use:**
Trained model to new_user reviews input to classify  as Positive or Negative.
Deployed model with streamlit  web UI for clear visual classification.
![imdb](https://github.com/user-attachments/assets/c6f42ac7-b56f-4032-b7f9-58c528e7a9a0)





