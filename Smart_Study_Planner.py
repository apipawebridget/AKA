session=[]

def classify_session(duration):
    if duration <30:
        return "short"
    elif duration<=90:
        return "Medium"
    else:
        return "Long"
def add_session():
    subject =input("enter subject name:")
    topic =input("enter topic:")
    date = input("enter day/date")
    while True:
        try:
            duration= int(input ("enter duration in minutes:"))
            if duration > 0:
                break
            else:
                print("duration must be > 0")
        except ValueError:
            print ("Invalid input, please enter a valid number!")
    session.append({"subject": subject, "topic": topic, "date": date, "duration": duration})
    print(">> session added succefully!")
def view_session():
    if not session:
        print ("no session logged yet.")
        return
    print("\n---All study session---")
    print(f"{'subject':<12} {'topic':<15} {'date':<12} {'duration':<10} {'type'}")
    print("-"*65)
    for s in session:
        type_=classify_session(s["duration"])
        print(f"{s['subject']:<12} {s['topic']:<15} {s['date']:<12} {s['duration']:<10} {type_}")
def search_by_subject():
    search=input("enter subject to search:").lower()
    found=[]
    total=0
    for s in session:
        if s["subject"].lower()==search:
            found.append(s)
            total+=s["duration"]
    if not found:
        print(f"No session found for subject '{search}'.")
    else:
        print(f"\nsession for {search}:")
        for s in found:
            print(f"-{s['topic']} on {s['date']}: {s['duration']} mins ({classify_session(s['duration'])})")
        print(f"total time for{search}: {total} mins ({total/60:.2f} hours)")
def study_statistics():
    if not session:
        print("no session to analyse.")
        return
    total_mins=sum(s["duration"] for s in session)
    print(f"\n total hours studied overall: {total_mins/60:.2f} hours")
    per_subject={}
    for s in session:
        per_subject[s["subject"]]=per_subject.get(s["subject"],0) + s["duration"]
    print("\ntotal hours per subject:")
    for sub,mins in per_subject.items():
        print(f"- {sub}: {mins/60:.2f} hours")
    weakest=min(per_subject, key=per_subject.get)
    print(f"\nweakest area (least time):{weakest} -{per_subject[weakest]}mins")
    longest= max(session,key=lambda x:x["duration"])
    print(f"longest session: {longest['subject']} -{longest['topic']} ({longest['duration']}mins)")
def save_session():
    with open ("study_log.txt","w") as f:
        for s in session: 
            f.write(f"{s['subject']},{s['topic']},{s['date']},{s['duration']}\n")
            print("session saved to study_log.txt")
def load_session():
    try:
        with open("study_log.txt", "r") as f:
            for line in f:
                subject,topic,date,duration=line.strip().split(",")
                session.append({
                    "subject":subject,
                    "topic":topic,
                    "date":date,
                    "duration":int(duration)
                })
        print("previous session loaded.")
    except FileNotFoundError:
        print("no previous log file found, starting fresh.")
    except Exception as e:
        print(f"error loading file:{e}")
def main():
    load_session()
    while True:
        print("\n=== SMART STUDY PLANNER===")
        print("1.add a new study session")
        print("2.view all sessions")
        print("3.search session by subject")
        print("4.view statistics")
        print("5.save and exit")

        choice=input("enter choice(1-5): ")
        if choice=="1":
            add_session()
        elif choice=="2":
            view_session()
        elif choice=="3":
            search_by_subject()
        elif choice=="4":
            study_statistics()
        elif choice=="5":
            save_session()
            print("goodbye!") 
            break
        else:
            print("invalid choice, please enter 1-5.")
if __name__=="__main__":
    main()                               

