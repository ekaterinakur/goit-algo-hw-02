from queue import Queue
import time
import random

MAX_QUEUE_SIZE = 5
REQUEST_LIMIT_PER_DAY = 30 # daily limit per one worker

class CustomerRequest:
    def __init__(self, id: int):
        self.id = id

def generate_request(queue: Queue, req_id: int):
    request = CustomerRequest(req_id)
    queue.put(request)
    print(f"New request added to the queue: {request.id}")
    time.sleep(0.2)

def process_request(queue: Queue):
    if not queue.empty():
        current = queue.get()
        print(f"Processing request {current.id}")
        time.sleep(0.2)
    else:
        print('Queue is empty')

def simulate_service_center():
    # queue = Queue(maxsize=MAX_QUEUE_SIZE)
    queue = Queue()

    req_id = 1

    try:
        while True:
            if random.random() > 0.3 and req_id <= REQUEST_LIMIT_PER_DAY:
                generate_request(queue, req_id)
                req_id += 1
            
            if random.random() > 0.3:
                process_request(queue)

            if req_id > REQUEST_LIMIT_PER_DAY and queue.empty():
                print('Daily limit reached')
                raise Exception()

    except:
        print('Terminated')

if __name__ == "__main__":
    simulate_service_center()
