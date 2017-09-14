from time import sleep
import RPi.GPIO as GPIO
import yaml

class raspRobot():
  def __init__( self, params ):
    self._motor_A = self._setupMotorGpio( params['motorA'] )
    self._motor_B = self._setupMotorGpio( params['motorB'] )
    self._speed = 0
    self._speedOffset = 0

  def setSpeed( self, speed ):
    print "speed", speed
    self._speed=speed
    self.updateSpeed()
    return

  def setDirection( self, speedOffset):
    print "new direction:", speedOffset
    self.updateSpeed()
    self._speedOffset=speedOffset
    return

  def updateSpeed( self ):
    self._motor_A.start( self._speed+self._speedOffset)
    self._motor_B.start( self._speed-self._speedOffset)
    return

  def _setupMotorGpio( self, params ):
      ''' Sets parameters for the IOs
          params: an object with the following properties
          params.dir_A: motor direction pin A
          params.dir_B: motor direction pin b
          params.pwm: pin to output PWM signals to (for speed)
          params.freq: frequency for PWM signal
          returns the motor object
      '''

      # set the pin numbering scheme
      GPIO.setmode(GPIO.BCM)

      # set pin for output
      GPIO.setup( params["dir_A"], GPIO.OUT )
      GPIO.setup( params["dir_B"], GPIO.OUT )
      GPIO.setup( params["pwm"], GPIO.OUT )
      motor = GPIO.PWM( params["pwm"], params["freq"] )

      return motor

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
      sleep( 3 )
      self._robot.setDirection( 0 )
      sleep( 1 )
      self._robot.setDirection( -1*dirOffset )
      sleep( 3 )
      self._robot.setDirection( 0 )
      sleep( 1 )

      loopCount = loopCount +1

if __name__ == "__main__":
  with open("config.yaml", 'r') as stream:
    try:
        params = yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)


  robot = raspRobot( params )
  robot.setSpeed(50)
  robot.setDirection(20)
  sleep (5)
#  rc = rc8( robot )
#rc.runLoop( 10 )
