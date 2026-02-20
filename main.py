# Write a Python function to filter a list of users using conditions like equals (=) and not equals (!=) on fields such as name, email,role and is_active.
# The function should support pagination using page and size parameters.
# Return the paginated result along with total record count and total pages.
users = [
    {"name":"Arun Kumar","email":"arun.kumar@mail.com","role":"admin","is_active":True},
    {"name":"Priya Sharma","email":"priya.sharma@mail.com","role":"user","is_active":True},
    {"name":"Vikram Singh","email":"vikram.singh@mail.com","role":"user","is_active":False},
    {"name":"Sneha Reddy","email":"sneha.reddy@mail.com","role":"manager","is_active":True},
    {"name":"Rahul Das","email":"rahul.das@mail.com","role":"user","is_active":True},
    {"name":"Karthik Raj","email":"karthik.raj@mail.com","role":"admin","is_active":False},
    {"name":"Meena Iyer","email":"meena.iyer@mail.com","role":"user","is_active":True},
    {"name":"Ajay Patel","email":"ajay.patel@mail.com","role":"user","is_active":True},
    {"name":"Divya Nair","email":"divya.nair@mail.com","role":"manager","is_active":False},
    {"name":"Suresh Babu","email":"suresh.babu@mail.com","role":"user","is_active":True},
    {"name":"Anjali Verma","email":"anjali.verma@mail.com","role":"admin","is_active":True},
    {"name":"Rohit Jain","email":"rohit.jain@mail.com","role":"user","is_active":False},
    {"name":"Pooja Kapoor","email":"pooja.kapoor@mail.com","role":"user","is_active":True},
    {"name":"Manoj Yadav","email":"manoj.yadav@mail.com","role":"manager","is_active":True},
    {"name":"Neha Gupta","email":"neha.gupta@mail.com","role":"user","is_active":True},
    {"name":"Santhosh Pillai","email":"santhosh.pillai@mail.com","role":"admin","is_active":False},
    {"name":"Lakshmi Devi","email":"lakshmi.devi@mail.com","role":"user","is_active":True},
    {"name":"Harish Rao","email":"harish.rao@mail.com","role":"user","is_active":True},
    {"name":"Deepak Mishra","email":"deepak.mishra@mail.com","role":"manager","is_active":True},
    {"name":"Swathi Krishnan","email":"swathi.krishnan@mail.com","role":"user","is_active":False},
    {"name":"Naveen Shetty","email":"naveen.shetty@mail.com","role":"admin","is_active":True},
    {"name":"Kavya Menon","email":"kavya.menon@mail.com","role":"user","is_active":True},
    {"name":"Varun Khanna","email":"varun.khanna@mail.com","role":"user","is_active":True},
    {"name":"Shalini Bose","email":"shalini.bose@mail.com","role":"manager","is_active":False},
    {"name":"Gokul Krishna","email":"gokul.krishna@mail.com","role":"user","is_active":True},
    {"name":"Tarun Arora","email":"tarun.arora@mail.com","role":"admin","is_active":True},
    {"name":"Nisha Kulkarni","email":"nisha.kulkarni@mail.com","role":"user","is_active":False},
    {"name":"Abhishek Sen","email":"abhishek.sen@mail.com","role":"user","is_active":True},
    {"name":"Ritika Chawla","email":"ritika.chawla@mail.com","role":"manager","is_active":True},
    {"name":"Yogesh Patil","email":"yogesh.patil@mail.com","role":"user","is_active":True}
]

filters={
    'role':('=','user'),
    'is_active':('!=',False)
}
def filter_user(user_list,filters,page,size):
    filtered_user=[]
    for user in user_list:
        match=True
        for field,condition in filters.items():
            operator,value=condition
            if operator=='=' and user[field]!=value:
                match=False
            elif operator=='!=' and user[field]==value:
                match=False
        if match:
                filtered_user.append(user)

    total_filtered_user=len(filtered_user)
    start=(page*size)-size
    # start=(page-1)*size (or) start= (page*size)-size
    end=start+size
    paginating=filtered_user[start:end]
    total_pages=(total_filtered_user+size-1)//size
    print(total_pages)
    return (
        paginating, 
        total_pages,
        total_filtered_user
    )

print(filter_user(users,filters,1,3))



