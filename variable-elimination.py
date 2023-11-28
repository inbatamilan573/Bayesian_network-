from pgmpy.models import BayesianNetwork
from pgmpy.inference import VariableElimination
from pgmpy.factors.discrete import TabularCPD

cpd_intelligence = TabularCPD(variable= 'Intelligence', variable_card= 2 ,
                              values=[[ 0.7],[0.3]])

cpd_difficulty = TabularCPD( variable='Difficulty',variable_card= 2 ,
                             values=[[ 0.6], [0.4]])

cpd_cgpa = TabularCPD(variable= 'CGPA', variable_card= 3,
                      values=[[0.3,0.4,0.2,0.35 ],[0.3,0.2,0.3,0.45],[0.4,0.4,0.5,0.2]] ,
evidence=['Intelligence','Difficulty' ] ,evidence_card=[2,2 ])

cpd_gre = TabularCPD(variable= 'GRE', variable_card= 2 ,values= [[0.8,0.2] ,
[0.2, 0.8] ] , evidence=[ 'Intelligence' ] , evidence_card =[2])

cpd_admit = TabularCPD( variable='Admit', variable_card = 2 ,
values=[[ 0.6,0.2,0.55,0.6,0.6,0.3],[0.4,0.8,0.45 ,0.4,0.4,0.7] ],evidence= ['CGPA','GRE' ], evidence_card= [3, 2] )

model = BayesianNetwork([('Intelligence', 'CGPA'),
('Difficulty', 'CGPA'),
('CGPA', 'Admit'),
('Intelligence', 'GRE'),
('GRE', 'Admit')])

model.add_cpds(cpd_intelligence,cpd_difficulty,cpd_cgpa,
cpd_gre,cpd_admit)

assert model.check_model()

inference = VariableElimination( model,elimination_order='enumeration')

result = inference.query(variables=['Intelligence'],evidence= {'Admit':1,'CGPA':2} )
print(" P(Intelligence | Admit= 1, CGPA= 2) : \n", result )
print("completed")
