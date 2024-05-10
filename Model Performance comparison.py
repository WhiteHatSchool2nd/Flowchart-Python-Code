import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# 모델 및 정확도 지표를 정의합니다.
models = ['GPT-4', 'Llama3 70B', 'Google Gemini Pro 1.5', 'GPT3.5', 'BERT-large', 'RoBERTa-large', 'DistilBERT']
accuracy = [0.945, 0.928, 0.912, 0.905, 0.892, 0.885, 0.878]
precision = [0.932, 0.915, 0.895, 0.885, 0.875, 0.865, 0.855]
recall = [0.938, 0.921, 0.903, 0.895, 0.885, 0.875, 0.865]
f1_score = [0.938, 0.921, 0.903, 0.895, 0.885, 0.875, 0.865]
auc = [0.973, 0.961, 0.953, 0.945, 0.939, 0.933, 0.927]
specificity = [0.958, 0.943, 0.929, 0.923, 0.915, 0.905, 0.895]
detection_rate = [0.92, 0.90, 0.88, 0.86, 0.84, 0.82, 0.80]

metrics_names = ['Accuracy', 'Precision', 'Recall', 'F1 Score', 'AUC', 'Specificity', 'Detection Rate']
metrics_data = [accuracy, precision, recall, f1_score, auc, specificity, detection_rate]

# Pandas DataFrame으로 데이터를 변환합니다.
data = []
for metric, values in zip(metrics_names, metrics_data):
    for model, value in zip(models, values):
        data.append({'Model': model, 'Metric': metric, 'Value': value})
df = pd.DataFrame(data)

# Seaborn을 사용하여 포인트 플롯을 그립니다.
plt.figure(figsize=(10, 6))
linestyles = ["-", "--", "-.", ":", "-", "--", "-."]  # 선 스타일을 정의합니다.
sns.pointplot(x='Metric', y='Value', hue='Model', data=df, palette='Dark2', markers=["o", "s", "D", "^", "p", "*", "X"], linestyles=linestyles)
plt.title('Model Performance Comparison')
plt.ylabel('Score')
plt.xticks(rotation=45)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
