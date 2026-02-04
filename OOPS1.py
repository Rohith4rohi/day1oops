# Class and object


class Instagram:
    def __init__(self,title, description,Creator_name,Location):  
        self.title = title
        self.description = description
        self.likes = 0
        self.Creator_name = Creator_name
        self.Location = Location
        self.comments=[]
    def display_title(self):
        return f"The title of the reel is {self.title}"
    def display_description(self):
        print("The description of the reel is ",self.description)
    def display_likes(self):
        print("The likes of the reel is ",self.likes)
    def liked(self):
        self.likes += 1
    def disliked(self):
        if self.likes > 0:
            self.likes-=1
    def display_Creator_name(self):
        print("The Creator name of the reel is ",self.Creator_name)
    def display_Location(self):
        print("The Location of the reel is ",self.Location) 
    def add_comments(self,comment):
        self.comments.append(comment)
    def display_comments(self):
        print("The Comment:",self.comments)   
    def delete_comments(self,comment):
        if comment in self.comments:
            last=self.comments.pop()   #for seleting last comment
 # or self.comments.remove(comment) and in down reel1.delete_comments("Great dance!")
            print("Deleted comment:",last)
    
    # def display_comment(self):
    #     if len(self.comments)==0:
    #         print("No comments yet.")
    #     else:
    #         print("The comments are:")   
    #         for comment in self.comments:
    #             print("-",comment) 
    # def add_comments(self,comment):
    #     self.comments.append(comment)
    # def delete_last_comment(self):
    #     temp_comment=self.comments.pop()
    #     print("Deleted comment:",temp_comment)
   


reel1=Instagram("dancing","dancing with friends","rohith","karnataka")
reel2=Instagram("Travelling","Travelling with friends","raj","kerala")
reel1.display_likes() 
print(reel1.display_title())
reel1.display_description()
reel1.display_Creator_name()
reel1.display_Location()
reel1.add_comments("Great dance!")
reel1.add_comments("Awesome moves!")
reel1.add_comments("Loved it!")
reel1.delete_comments()
reel1.display_comments()

print(id(reel1))
print(id(reel2))

# reel2.display_likes() 
# print(reel1.display_title())
# reel2.display_description()
# reel2.display_Creator_name()
# reel2.display_Location()
# reel2.add_comments("Great dance!")
# reel2.add_comments("Awesome moves!")
# reel2.add_comments("Loved it!")
# reel2.delete_comments("Great dance!")
# reel2.display_comments()
