import psutil
from win10toast import ToastNotifier
import sched, time

toaster = ToastNotifier()

def checkPIA(sc):
    foundpia = False

    allids = psutil.pids()
    for id in allids:
        try:
            p = psutil.Process(id)
            if p.name() == "pia_manager.exe":
                print("id " + str(id))
                foundpia = True
        except:
            print("error")

    if foundpia == False:
        toaster.show_toast(
            "Hey, you! You're awesome.",
            "That's not why I'm here though. Your VPN is off. You may want to turn that bad boy back on.",
            icon_path="pia3.ico",
            duration=25)

    s.enter(600, 1, checkPIA, (sc,))

if __name__ == "__main__":
    s = sched.scheduler(time.time, time.sleep)
    s.enter(600, 1, checkPIA, (s,))
    s.run()