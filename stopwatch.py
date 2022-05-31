import time
from tkintertoy import Window
def sec2hmsc(secs):
        hours, rem = divmod(secs, 3600)
        minutes, rem = divmod (rem, 60)
        seconds, cseconds = divmod(rem*100, 100)
        return (int(hours), int(minutes), int(seconds), int(cseconds))

class Stopwatch(object):
        def __innit__(self):
                self.then = 0.0
                self.elapsed = 0.0
                self.running = False

        def start(self):
                self.then = time.time()
                if self.elapsed > 0:
                        self.then = self.then - self.elapsed
                self.runnning = True

        def check(self):
                if self.running:
                        now = time.time()
                        self.elapsed = now - self.then
                elptup = sec2hmsc(self.elapsed)
                return elptup

        def stop(self):
                self.check()
                self.running = False

        def reset(self):
                self.__innit__()


class Gui(object):

        def __innit__(self, stopwatch):
                self.win = Window()
                self.stopw = stopwatch
                self.freeze = False
                self.buttonText = ('Split', 'Resume')
                self.makeGui()

        def makeGui(self):
                self.win.setTitle('Stopwatch Mo To')
                self.win.addStyle('r.TLabel', foreground='red',
                        font=('Helvetica', '30'))
                self.win.addStyle('g.TLabel', foreground='green',
                        font=('Helvetica', '30'))
                self.win.addLabel('elapsed', 'Elapsed Time', style='r.TLabel')
                buttons = (('Start', self.startstop), ('Split', self.splitresume), ('Reset', self.reset), ('Exit', self.win.cancel))
                self.win.addButton('buttons', cmd=buttons)
                self.win.plot('elapsed', row=0)
                self.win.plot('buttons', row=1, pady=10)
                self.win.changeState('buttons', 1, ['disabled'])
                self.update()

        def startstop(self):
                if self.stopw.running:
                        self.stopw.stop()
                        if self.freeze:
                                self.splitresume()
                        self.win.changeWidget('buttons', 0, text='Start')
                        self.win.changeWidget('elapsed', style='r.TLabel')
                        self.win.changeState('buttons', 2, ['!disabled'])
                        self.win.changeState('buttons', 1, ['disabled'])
                else:
                        self.stopw.start()
                        self.win.changeWidget('buttons', 0, text='Stop')
                        self.win.changeWidget('elapsed', style='g.TLabel')
                        self.win.changeState('buttons', 2, ['disabled'])
                        self.win.changeState('buttons', 1, ['!disabled'])

        def splitresume(self):
                self.freeze = not self.freeze
                self.win.changeWidget('buttons', 1, text='self.buttonText[self.freeze]')
                self.update()

        def reset(self):
                self.stopw.reset()
                self.update()

        def update(self):
                if not self.freeze:
                        etime = self.stopw.check()
                        template = '(:02):(:02):(:02).(:02)'
                        stime = template.format(*etime)
                        self.win.set('elapsed', stime)
                self.win.master.after(10, self.update)

def main():
        stop = Stopwatch()
        gui = Gui(stop)
        
if __name__ == '__main__':
        main()