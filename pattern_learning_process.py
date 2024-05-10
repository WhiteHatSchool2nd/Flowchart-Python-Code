from graphviz import Digraph

# 그래프 생성 
dot = Digraph(comment='Pattern Learning and Accuracy Improvement Process')

# 노트 추가 
dot.node('A', 'Normal Activity Pattern Learning\n(Analyze data to learn normal activity patterns)', shape='box')
dot.node('B', 'Anomalous Activity Pattern Learning\n(Llama 3 Fine-tuning)\n(Analyze past anomalous behaviors to identify abnormal patterns)', shape='box')
dot.node('C', 'Accuracy Improvement\n(Continuously improve model detection accuracy based on learned patterns)', shape='box')

# 엣지 추가
dot.edges(['AB', 'BC'])

# 그래프 파일로 렌더링 (PDF)
dot.render('pattern_learning_process', view=True)


