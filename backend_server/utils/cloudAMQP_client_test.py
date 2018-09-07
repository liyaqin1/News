from cloudAMQP_client import CloudAMQPClient

CLOUDAMQP_URL = "amqp://zburscyu:rEI-fKKsLoMqCU9pItGXyFQwrX-UbCww@otter.rmq.cloudamqp.com/zburscyu"

TEST_QUEUE_NAME = 'test_ttt'

def test_basic():
    client = CloudAMQPClient(CLOUDAMQP_URL, TEST_QUEUE_NAME)

    sentMsg = {'test_ttt':'demo'}
    client.sendMessage(sentMsg)
    client.sleep(10)
    receivedMsg = client.getMessage()
    assert sentMsg == receivedMsg
    print 'test_basic passed!'

if __name__ == '__main__':
    test_basic()
