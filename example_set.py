from collections import deque

class Event:
    def __init__(self,input=deque(),sharedInput=None,target=deque(),
                 sharedTargets=None,maxTime=None,minTime=None,graceTime=None,
                 defaultInput=None,activeInput=None,detaultTarget=None,
                 activeTarget=None,proc=None,example=None,ext=None):
        self.input = input
        self.sharedInput = sharedInput
        self.target = target
        self.sharedTargets = sharedTargets
        self.maxTime = maxTime
        self.minTime = minTime
        self.graceTime = graceTime
        self.defaultInput = defaultInput
        self.activeInput = activeInput
        self.detaultTarget = detaultTarget
        self.activeTarget = activeTarget
        self.proc = proc
        self.example = example
        self.ext = ext
        self.updateTime()

    def updateTime(self):
        if self.maxTime is None:
            self.maxTime = self.example.set.maxTime
        if self.minTime is None:
            self.minTime = self.example.set.minTime
        if self.graceTime is None:
            self.graceTime = self.example.set.graceTime

class Example:
    def __init__(self,name=None,num=None,numEvents=None,event=[],set=None,nxt=None,
                 ext=None,freq=1.0,prob=None,proc=None):
        self.name = name
        self.num = num
        self.numEvents = numEvents
        self.event = event
        self.set = set
        self.nxt = nxt
        # a pointer to the example extension structure, not in this file
        self.ext = ext
        self.freq = freq
        self.prob = prob
        # Tcl_obj
        self.proc = proc

class ExampleSet:
    def __init__(self,name,num,mode,numExamples,currentExampleNum,currentExample,
                 firstExample,lastExample,maxTime,minTime,graceTime,defaultInput,
                 activeInput,defaultTarget,activeTarget,numGroupNames,maxGroupNames,
                 groupName=[],numEvents=None,ext=None,example=None,permuted=None,pipExample=None,
                 pipeParser=None,pipeLoop=True,pipeExampleNum=None,proc=None,
                 chooseExample=None, loadEvent = None, loadExample =None,nextExample=None):
        self.name = name
        self.num = num
        self.numExamples = numExamples
        self.currentExampleNum = currentExampleNum
        self.currentExample = currentExample
        self.firstExample = firstExample
        self.lastExample = lastExample
        self.maxTime = maxTime
        self.minTime = minTime
        self.graceTime = graceTime
        self.defaultInput = defaultInput
        self.activeInput = activeInput
        self.defaultTarget = defaultTarget
        self.activeTarget = activeTarget
        self.numGroupNames = numGroupNames
        self.maxGroupNames = maxGroupNames
        self.groupName = groupName
        self.numEvents = numEvents
        self.ext = ext
        self.example = example
        self.permuted = permuted
        self.pipExample = pipExample
        self.pipeParser = pipeParser
        self.pipeLoop = pipeLoop
        self.pipeExampleNum = pipeExampleNum
        self.proc = proc
        self.chooseExample = chooseExample
        self.loadEvent = loadEvent
        self.loadExample = loadExample
        self.nextExample = nextExample