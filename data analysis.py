# Digraph 객체 생성
dot = Digraph()

# 노드 색상 정의 
node_colors = {
    'preprocessing': '#CCCCCC',         # Light Grey
    'unsupervised_learning': '#CCCCCC', # Light Grey
    'model_training': '#CCCCCC'         # Light Grey
}

# 설명, 노드 추가
dot.node('preprocessing', '데이터 전처리\n- Raw 데이터를 정제하고 전처리합니다.\n- 결측값을 처리합니다.\n- 특성 엔지니어링을 수행합니다.')
dot.node('unsupervised_learning', '비지도 학습\n- 데이터의 패턴과 이상을 감지합니다.\n- 유사한 데이터 포인트를 군집화합니다.')
dot.node('model_training', '모델 훈련\n- 기계 학습 모델을 훈련합니다.\n- 전처리된 데이터를 사용하여 모델을 훈련합니다.')

# 간선 추가
dot.edges([
    ('preprocessing', 'unsupervised_learning'),
    ('unsupervised_learning', 'model_training')
])

# 그래프 속성 설정 
dot.attr(label='Data Analysis Flowchart', fontsize='14', fontname='Arial')

# 그래프 렌더링 및 표시
dot.view(cleanup=True)
