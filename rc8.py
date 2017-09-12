from time import sleep

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
