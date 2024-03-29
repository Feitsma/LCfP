"Exercise 11.1.12 of How to Think Like a ComputerScientist: Learning with Python 3Documentation1"

import math
import datetime
import time

class SMS_store:
    """This class handles storage of SMS messages in tuples of (has_been_viewed, from_number, time_arrived, text_of_sms)"""

    def __init__(self):
        """Initiates the form of the inbox. In this case a list with tuples holding info on: (has_been_viewed, from_number, time_arrived, text_of_sms)"""
        self.inbox = []

    def add_new_arrival(self, from_number , text_of_sms):
        """Adds new arrival based on given information on number, text of sms and adds automatically if it is read and time"""
        ti = time.gmtime()
        local_time = time.asctime(ti)
        self.inbox.append((False, from_number, local_time, text_of_sms))

    def message_count(self):
        """Retuns nr. of messages in inbox"""
        return len(self.inbox)

    def get_unread_indexes(self):
        """This method returns a list with indices of unread messages"""
        unread_messages_list = []
        i=0
        for messages in self.inbox:
            if messages[0] == False:
                unread_messages_list.append(i)
                i = i+1
            else:
                i = i+1
        return unread_messages_list

    def get_messages(self, message_index):
        """Request an message"""
        try: #check if index of requested message does exist
            self.inbox[message_index]
            if self.inbox[message_index][0] == False:
                msg = list(self.inbox[message_index])
                msg[0] = True
                self.inbox[message_index] = tuple(msg)
            return self.inbox[message_index][1], self.inbox[message_index][2], self.inbox[message_index][3]
        except IndexError:
            return None

    def delete(self, message_index):
        """Deletes message at index """
        self.inbox.pop(message_index) #pop removes entry from list

    def clear(self):
        """Clears whole inbox"""
        self.inbox = [] #overwrites inbox with empty list


#some test code
my_inbox = SMS_store() #initiate my_inbox in SMS_store class
my_inbox.add_new_arrival('1','hey')
my_inbox.add_new_arrival('2', 'Hey, works this?')
print(my_inbox.get_unread_indexes()) #give list with indices of unread messages
print(my_inbox.get_messages(0)) #request to print message at index 0
my_inbox.clear() #empty inbox