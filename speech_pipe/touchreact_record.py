import qi
import functools
import sys
from recording import Recording_thread
from naoqi import ALProxy

robotIP = str(sys.argv[1])
# robotIP = "192.168.8.160"

class ReactToTouch(object):
    """ A simple module able to react
        to touch events.
    """
    def __init__(self, app):
        super(ReactToTouch, self).__init__()

        # Get the services ALMemory, ALTextToSpeech.
        app.start()
        session = app.session
        self.memory_service = session.service("ALMemory")
        self.tts = session.service("ALTextToSpeech")
        # Connect to an Naoqi1 Event.
        self.touch = self.memory_service.subscriber("TouchChanged")
        self.id = self.touch.signal.connect(functools.partial(self.onTouched, "TouchChanged"))

    def onTouched(self,strVarName, value):
        print("recording")
        """ This will be called each time a touch
        is detected.

        """
        # Disconnect to the event when talking,
        # to avoid repetitions
        self.touch.signal.disconnect(self.id)

        touched_bodies = []
        for p in value:
            if p[1]:
                touched_bodies.append(p[0])

        #self.say(touched_bodies)
        Recording_thread(robotIP)
        # Reconnect again to the event
        self.id = self.touch.signal.connect(functools.partial(self.onTouched, "TouchChanged"))



if __name__ == "__main__":
    try:
        # Initialize qi framework.
        #change IP below
        connection_url = "tcp://" + robotIP + ":" + "9559"
        app = qi.Application(["ReactToTouch", "--qi-url=" + connection_url])
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + robotIP + "\" on port " + "9559" +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    react_to_touch = ReactToTouch(app)
    
    app.run()
