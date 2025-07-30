import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    """
    Unit tests for the EmotionDetection package.
    
    Tests the emotion_detector function with various text inputs to verify
    correct emotion detection and dominant emotion identification.
    """
    
    def test_joy_emotion(self):
        """Test detection of joy as dominant emotion."""
        statement = "I am glad this happened"
        result = emotion_detector(statement)
        
        # Check that result is not None and has expected structure
        self.assertIsNotNone(result)
        self.assertIn('dominant_emotion', result)
        
        # Check that dominant emotion is joy
        self.assertEqual(result['dominant_emotion'], 'joy')
        
        # Check that all emotion scores are present and are numbers (not None)
        emotions = ['anger', 'disgust', 'fear', 'joy', 'sadness']
        for emotion in emotions:
            self.assertIn(emotion, result)
            self.assertIsNotNone(result[emotion])
            self.assertIsInstance(result[emotion], (int, float))
            
        # Check that joy has the highest score
        joy_score = result['joy']
        other_scores = [result[emotion] for emotion in emotions if emotion != 'joy']
        self.assertTrue(all(joy_score >= score for score in other_scores))
    
    def test_anger_emotion(self):
        """Test detection of anger as dominant emotion."""
        statement = "I am really mad about this"
        result = emotion_detector(statement)
        
        # Check that result is not None and has expected structure
        self.assertIsNotNone(result)
        self.assertIn('dominant_emotion', result)
        
        # Check that dominant emotion is anger
        self.assertEqual(result['dominant_emotion'], 'anger')
        
        # Check that all emotion scores are present and are numbers (not None)
        emotions = ['anger', 'disgust', 'fear', 'joy', 'sadness']
        for emotion in emotions:
            self.assertIn(emotion, result)
            self.assertIsNotNone(result[emotion])
            self.assertIsInstance(result[emotion], (int, float))
            
        # Check that anger has the highest score
        anger_score = result['anger']
        other_scores = [result[emotion] for emotion in emotions if emotion != 'anger']
        self.assertTrue(all(anger_score >= score for score in other_scores))
    
    def test_disgust_emotion(self):
        """Test detection of disgust as dominant emotion."""
        statement = "I feel disgusted just hearing about this"
        result = emotion_detector(statement)
        
        # Check that result is not None and has expected structure
        self.assertIsNotNone(result)
        self.assertIn('dominant_emotion', result)
        
        # Check that dominant emotion is disgust
        self.assertEqual(result['dominant_emotion'], 'disgust')
        
        # Check that all emotion scores are present and are numbers (not None)
        emotions = ['anger', 'disgust', 'fear', 'joy', 'sadness']
        for emotion in emotions:
            self.assertIn(emotion, result)
            self.assertIsNotNone(result[emotion])
            self.assertIsInstance(result[emotion], (int, float))
            
        # Check that disgust has the highest score
        disgust_score = result['disgust']
        other_scores = [result[emotion] for emotion in emotions if emotion != 'disgust']
        self.assertTrue(all(disgust_score >= score for score in other_scores))
    
    def test_sadness_emotion(self):
        """Test detection of sadness as dominant emotion."""
        statement = "I am so sad about this"
        result = emotion_detector(statement)
        
        # Check that result is not None and has expected structure
        self.assertIsNotNone(result)
        self.assertIn('dominant_emotion', result)
        
        # Check that dominant emotion is sadness
        self.assertEqual(result['dominant_emotion'], 'sadness')
        
        # Check that all emotion scores are present and are numbers (not None)
        emotions = ['anger', 'disgust', 'fear', 'joy', 'sadness']
        for emotion in emotions:
            self.assertIn(emotion, result)
            self.assertIsNotNone(result[emotion])
            self.assertIsInstance(result[emotion], (int, float))
            
        # Check that sadness has the highest score
        sadness_score = result['sadness']
        other_scores = [result[emotion] for emotion in emotions if emotion != 'sadness']
        self.assertTrue(all(sadness_score >= score for score in other_scores))
    
    def test_fear_emotion(self):
        """Test detection of fear as dominant emotion."""
        statement = "I am really afraid that this will happen"
        result = emotion_detector(statement)
        
        # Check that result is not None and has expected structure
        self.assertIsNotNone(result)
        self.assertIn('dominant_emotion', result)
        
        # Check that dominant emotion is fear
        self.assertEqual(result['dominant_emotion'], 'fear')
        
        # Check that all emotion scores are present and are numbers (not None)
        emotions = ['anger', 'disgust', 'fear', 'joy', 'sadness']
        for emotion in emotions:
            self.assertIn(emotion, result)
            self.assertIsNotNone(result[emotion])
            self.assertIsInstance(result[emotion], (int, float))
            
        # Check that fear has the highest score
        fear_score = result['fear']
        other_scores = [result[emotion] for emotion in emotions if emotion != 'fear']
        self.assertTrue(all(fear_score >= score for score in other_scores))
    
    def test_output_format(self):
        """Test that the output format is correct for any input."""
        statement = "This is a test statement"
        result = emotion_detector(statement)
        
        # Check that result is a dictionary
        self.assertIsInstance(result, dict)
        
        # Check that all required keys are present
        required_keys = ['anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion']
        for key in required_keys:
            self.assertIn(key, result)
        
        # Check that there are no extra keys
        self.assertEqual(len(result), len(required_keys))
        
        # If not None, emotion scores should be between 0 and 1
        for emotion in ['anger', 'disgust', 'fear', 'joy', 'sadness']:
            score = result[emotion]
            if score is not None:
                self.assertIsInstance(score, (int, float))
                self.assertGreaterEqual(score, 0)
                self.assertLessEqual(score, 1)
    
    def test_empty_string(self):
        """Test behavior with empty string input."""
        result = emotion_detector("")
        
        # Should still return the correct format
        self.assertIsInstance(result, dict)
        required_keys = ['anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion']
        for key in required_keys:
            self.assertIn(key, result)
    
    def test_multiple_statements_consistency(self):
        """Test that the same input produces consistent results."""
        statement = "I am glad this happened"
        
        # Run the same test multiple times
        results = []
        for _ in range(3):
            result = emotion_detector(statement)
            results.append(result)
        
        # All results should be identical
        for i in range(1, len(results)):
            self.assertEqual(results[0], results[i])

def run_specific_tests():
    """
    Run tests for the specific statements and print detailed results.
    This function provides a more detailed view of the test results.
    """
    test_cases = [
        ("I am glad this happened", "joy"),
        ("I am really mad about this", "anger"),  
        ("I feel disgusted just hearing about this", "disgust"),
        ("I am so sad about this", "sadness"),
        ("I am really afraid that this will happen", "fear")
    ]
    
    print("Running Emotion Detection Tests")
    print("=" * 50)
    
    for statement, expected_emotion in test_cases:
        print(f"\nTesting: '{statement}'")
        print(f"Expected dominant emotion: {expected_emotion}")
        
        try:
            result = emotion_detector(statement)
            if result and result['dominant_emotion'] is not None:
                print(f"Actual dominant emotion: {result['dominant_emotion']}")
                print(f"Emotion scores: {dict(list(result.items())[:-1])}")  # All except dominant_emotion
                
                if result['dominant_emotion'] == expected_emotion:
                    print("✅ TEST PASSED")
                else:
                    print("❌ TEST FAILED")
            else:
                print("❌ ERROR: Function returned None or invalid result")
                print(f"Result: {result}")
        except Exception as e:
            print(f"❌ ERROR: Exception occurred: {str(e)}")
        
        print("-" * 30)

if __name__ == '__main__':
    # Run the detailed test function first
    run_specific_tests()
    
    print("\n" + "=" * 50)
    print("Running Unit Tests")
    print("=" * 50)
    
    # Run the unit tests
    unittest.main(verbosity=2)