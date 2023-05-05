import unittest
from sentiment import ProblemRecognition

class TestProject(unittest.TestCase):

    def test_sth(self):
        analyzeProblems = ProblemRecognition()
        self.assertIsInstance(analyzeProblems.getNegativePosts([{'headline':'some headline'}]), list)



if __name__ == '__main__':
    unittest.main()