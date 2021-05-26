class ticket:
    def __init__(self,total_ticket):
        self.total_ticket=total_ticket
    def Ticket(self,num):
        while True:
            no_of_tickets_needed=int(input("enter the no of ticket needed "))
            self.total_ticket=self.total_ticket-no_of_tickets_needed
            if self.total_ticket>=num:
                print( self.total_ticket)
            else:
                print("insufficient ticket")
                break

train_ticket=ticket(50)
train_ticket.Ticket(0)