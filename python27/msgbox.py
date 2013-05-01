#Ορισμός της κλάσης ball:
class ball:
      def bounce(self):
          if self.direction==’down’:
             self.direction=’up’
my_ball=ball() #Δημιουργία αντικειμένου
#Θέτουμε τιμές στα αυθαίρετα πεδία του:
my_ball.direction=’down’
my_ball.color=’green’
my_ball.size=’middle’
print “Μόλις δημιούργησα μια μπάλα με:”
print “Κατεύθυνση:”,my_ball.direction
print “Χρώμα:”,my_ball.color
print “Μέγεθος:”,my_ball.size
print “Τώρα της κάνω αναπήδηση!”
my_ball.bounce()
print “Νέα κατεύθυνση:”,my_ball.direction
