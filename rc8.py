from time import sleep
import RPi.GPIO as GPIO
import yaml

with open("config.yaml", 'r') as stream:
    try:
        print(yaml.load(stream))
    except yaml.YAMLError as exc:
        print(exc)

def setupMotorGpio( params ):
    ''' Sets parameters for the IOs

        params: an object with the following properties
        params.pin_dir_a: motor direction pin A
        params.pin_dir_b: motor direction pin b
        params.pin_pwma: pin to output PWM signals to (for speed)
        params.freq: frequency for PWM signal
        params: an object with the following properties
        params.pin_dir_B: motor direction pin A
        params.pin_dir_A: motor direction pin b
        params.pin_pwmb: pin to output PWM signals to (for speed)
        params.freq: frequency for PWM signal

        returns the motor object
    '''

    # set the pin numbering scheme
    GPIO.setmode(GPIO.BCM)

    # set pin for output
    GPIO.setup( params.pin_dir_a, GPIO.OUT )
    GPIO.setup( params.pin_dir_a, GPIO.OUT )
    GPIO.setup( params.pin_pwma, GPIO.OUT )
    GPIO.setup( params.pin_dir_A, GPIO.OUT )
    GPIO.setup( params.pin_dir_B, GPIO.OUT )
    GPIO.setup( params.pin_pwmb, GPIO.OUT )

    return motor

class mockRobot():
  def setSpeed( self, speed ):
    print "speed", speed
    return

  def setDirection( self, speedOffset):
    print "new direction:", speedOffset
    return

class rc8():
  def __init__( self, robot ):
    self._robot = robot

  def runLoop( self, count ):
    loopCount = 0

    speed = 50
    dirOffset = 20

    self._robot.setSpeed( 50 )

    while( loopCount < count ):
      self._robot.setDirection( dirOffset )
      sleep( 5 )
      self._robot.setDirection( 0 )
      sleep( 1 )
      self._robot.setDirection( -1*dirOffset )
      sleep( 3 )
      self._robot.setDirection( 0 )
      sleep( 1 )

      loopCount = loopCount +1

if __name__ == "__main__":
  robot = mockRobot()
  rc = rc8( robot )
rc.runLoop( 10 )