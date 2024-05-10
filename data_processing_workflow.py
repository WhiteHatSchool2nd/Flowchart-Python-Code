from graphviz import Digraph

# 그래프 생성
dot = Digraph(comment='Data Processing and Model Fine-tuning Workflow')

# 노드 생성
dot.node('A', 'Step 1: Data Collection', shape='box')
dot.node('B', 'Step 2: Llama 3 Model Fine-tuning', shape='box')
dot.node('C', 'Step 3: Identify Normal and Abnormal Activity Patterns', shape='box')

# 엣지 추가
dot.edges(['AB', 'BC'])

# 그래프 파일로 렌더링 (PDF)
dot.render('data_processing_workflow', view=True, format='pdf')
