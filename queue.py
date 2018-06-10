import unittest

# Represents a FIFO data structure (queue) of bounded size.
class Queue(object):
    
    def __init__(self, n):
        self.n = n
        self.listt = [None] * n
        self.counter = 0 # no of elements in the array
        self.start = 0
        
    def enqueue(self, item):
        if self.full():
            raise Exception('Cannot enqueue. Bound reached.')
        self._add_item_to_queue(item)
            
    def dequeue(self):
        if self.empty():
            raise Exception('Cannot dequeue. No items.')
        out = self._earliest_item()
        self._discard_earliest_item_from_queue()
        return out
    
    def front(self):
        if self.empty():
            raise Exception('Nothing at the front of queue.')
        return self._earliest_item()
    
    def empty(self):
        return self.counter == 0
    
    def full(self):
        return self.counter == self.n
    
    def _next_position(self):
        return self._wrapped(self.start + self.counter)
    
    def _add_item_to_queue(self, item):
        self.listt[self._next_position()] = item
        self.counter += 1
        
    def _earliest_item(self):
        return self.listt[self.start]
    
    def _discard_earliest_item_from_queue(self):
        self.start = self._wrapped(self.start + 1)
        self.counter -= 1
    
    def _wrapped(self, x):
        return x % self.n
        
class QueueTest(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def test_that_newly_created_queue_is_empty(self):
        q = Queue(100)
        self.assertEqual(q.empty(), True)

    def test_that_after_filling_up_queue_it_is_full(self):
    	q = Queue(2)
    	q.enqueue(0)
    	q.enqueue(1)
    	self.assertEqual(q.full(), True)

    def test_that_dequeuing_an_empty_queue_throws(self):
    	q = Queue(2)
    	self.assertRaises(Exception, q.dequeue)

    def test_that_enqueuing_a_full_queue_throws(self):
    	q = Queue(2)
    	q.enqueue(10)
    	q.enqueue(11)
    	self.assertRaises(Exception, q.enqueue, 13)
    
    def test_that_enqueuing_just_after_dequeuing_a_full_queue_works(self):
    	q = Queue(3)
    	q.enqueue(1)
    	q.enqueue(2)
    	q.enqueue(3)
    	q.dequeue()
    	q.enqueue(4)
    	self.assertEqual(q.front(), 2)
    	self.assertEqual(q.dequeue(), 2)

    def test_that_enqueuing_a_full_queue_just_after_fully_dequeuing_it_works(self):
        q = Queue(3)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.dequeue()
        q.dequeue()
        q.dequeue()
        q.enqueue(4)
        q.enqueue(5)
        q.enqueue(6)
        self.assertEqual(q.front(), 4)
        self.assertEqual(q.dequeue(), 4)

if __name__ == '__main__':
    unittest.main()
