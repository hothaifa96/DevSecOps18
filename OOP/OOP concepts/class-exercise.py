# from abc import abstractclassmethod, ABC
#
#
# #           -------
# #           Friends
# #           -------
# #
# #  -------          -------
# #   Joey            chandler
# #  -------          -------
#
#
# class Friend(ABC):
#     def __init__(self, name, catchphrase):
#         self.name = name
#         self.catchphrase = catchphrase
#         self.acting_job = []
#         self.sandwich_count = 0
#
#     @abstractclassmethod
#     def say_the_catchphrase(self):
#         pass
#
#
# class JoyLikeFriend(Friend):
#     def __init__(self, name, catchphrase):
#         super().__init__(name, catchphrase)
#
#     def say_the_catchphrase(self):
#         print(f'scream {self.catchphrase}')
# class ChandlerLikeFriend(Friend):
#     def __init__(self, name, catchphrase,jokes):
#         super().__init__(name, catchphrase)
#         self.jokes =[]
#     def say_the_catchphrase(self):
#         print(f'tell a joke and , {self.catchphrase}')
#     def tell a jp