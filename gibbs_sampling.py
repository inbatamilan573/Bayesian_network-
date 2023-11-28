from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD

# Defining the model structure.
model = BayesianModel([('cloudy', 'rain'),
                                    ('cloudy', 'sprinkler'),
                                    ('sprinkler', 'wetgrass'),
                                    ('rain', 'wetgrass')])

 # Defining individual CPDs.
cpd_c =TabularCPD('cloudy', 2, [[0.5], [0.5]])
cpd_s= TabularCPD('sprinkler', 2, [[0.5, 0.9],[0.5, 0.1]],evidence=['cloudy'],evidence_card=[2])
cpd_r = TabularCPD('rain', 2, [[0.8, 0.2],[0.2, 0.8]],evidence=['cloudy'],evidence_card=[2])
cpd_w =TabularCPD('wetgrass', 2, [[1,0.1,0.1,0.01],[0,0.9,0.9,0.99]],evidence=['rain', 'sprinkler'],evidence_card=[2, 2])

# Associating the CPDs with the network
model.add_cpds(cpd_c, cpd_s, cpd_r, cpd_w)
model.check_model()
print()

from pgmpy.sampling import GibbsSampling
gibbs_chain = GibbsSampling(model)

sample = gibbs_chain.sample(size=80)
print(sample)

from pgmpy.inference import ApproxInference
infer = ApproxInference(model)
result = infer.query(variables=["wetgrass"],
                    evidence={"sprinkler":0, "rain":1},
                     n_samples=1000)
print(result)
event = {'cloudy': True, 'rain': True, 'sprinkler': False, 'wetgrass': True}


