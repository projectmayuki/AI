# @author Mayuki
# @brief SampleAI
# @file SampleAI.py

class SampleAI:

    def __init__(self):
        self._is_stop = False
    # __init__

    def execute(self):

        cnt = 0
        while True:
            if self._is_stop == True:
                break

            cnt = cnt + 1
            if cnt % 100 == 0:
                print(cnt)
            if cnt == 1000:
                self.stop()
        # while True
    # execute

    def stop(self):
        self._is_stop = True
    # stop
