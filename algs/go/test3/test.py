import unittest, pickle, util, simplenet, resnet
import numpy as np

class BasicTest(unittest.TestCase):
    def testBla(self):
        state, pi, reward = pickle.load(open("testdata.pkl"))
        state._create_neighbors_cache()

        lm = state.get_legal_moves()
        print len(lm) > 10
        
        print util.pprint_board(state.board)
        
        res = util.to_pi_mat(pi)
        
        self.assertTrue(res[0]==0)

        net = simplenet.PolicyValue(simplenet.PolicyValue.create_network())
        
        res = net.eval_value_state(state)

        self.assertTrue(np.abs(res) > 0.0)

        net = resnet.PolicyValue(resnet.PolicyValue.create_network())

        self.assertTrue(np.abs(res) > 0.0)
        
        
if __name__ == "__main__": 

    unittest.main()
    
