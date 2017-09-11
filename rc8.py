

class mockRobot():
  def setSpeed( self, speed ):
    print "speed", speed
    return

  def serDirection( SpeedOFfset):
    print "new direction:", speedOffset
    return
        
class rc8():
  def __init__( robot ):
    self._robot = robot
    
  def runLoop( count ):
    loopCount = 0
     
    speed = 50
    dirOffset = 20
     
    self._robot.setSpeed( 50 )
    
    while( loopCount < count ):
      setDirection( dirOffset )
      sleep( 5 )
      setDirection( 0 )
      wait( 1 )
      setDirection( -1*dirOffset )
      wait( 3 )
      setDirectione( 0 )
      wait( 1 )
      
      loopcount = loopcount +1

if __name__ == "__main__":
  robot = mockRobot()
  rc = rc8( robot )
  rc.runLoop( 10 )
