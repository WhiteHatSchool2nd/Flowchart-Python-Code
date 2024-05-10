from graphviz import Digraph

dot = Digraph(comment='The Further Improved Abnormal Behavior Process')

# 노드 추가
dot.node('A', 'Start')
dot.node('B', 'Classify Behavior')
dot.node('C', 'Behavior: Alert')
dot.node('D', 'Send Alert to Admin')
dot.node('E', 'Behavior: Threat')
dot.node('F', 'Block Behavior')
dot.node('G', 'Monitor Behavior')
dot.node('H', 'End')

# 엣지 추가
dot.edges(['AB'])
dot.edge('B', 'C', 'Alert')
dot.edge('B', 'E', 'Threat')
dot.edge('B', 'H', 'Normal')  
dot.edges(['CD', 'CE', 'CG'])  
dot.edge('E', 'F', 'Threat Detected')  
dot.edge('G', 'F', 'Threat Detected')  
dot.edge('F', 'H', 'After Blocking')  

# 그래프 파일로 렌더링 (PDF)
dot.render('further_improved_abnormal_behavior_process', view=True)
