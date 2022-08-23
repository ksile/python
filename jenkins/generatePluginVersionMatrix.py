import csv
files = ["jenkins-eval-plugins.txt","jenkins-tst-plugins.txt","jenkins-dev-plugins.txt","jenkins-prod-plugins.txt"]

class plugins():
    def __init__(self):
        self.__plugins = {}
    # position 0 EVAL, 1 TST, 2 DEV, 3 PROD    
    def add(self,name,version,arrayPosition):
        if name in self.__plugins:
            versions = self.__plugins[name]
            versions[arrayPosition] = version
            self.__plugins[name] = versions
        else:
            versions = ["-","-","-","-"]
            versions[arrayPosition] = version
            self.__plugins[name] = versions
    def writeCSV(self):
        with open('jenkins-plugin-version-matrix.csv', 'w', newline='') as csvfile:
            pluginwriter = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for plugin in self.__plugins:
                row = self.__plugins[plugin]
                row.insert(0,plugin)
                pluginwriter.writerow(row)
    
pluginDict = plugins()
position = 0

for pluginFile in files:
    file = open(pluginFile, "r")
    for line in file:
        data = line.strip().split(": ")
        name = data[0]
        version = data[1]
        pluginDict.add(name, version, position)
    position = position + 1

pluginDict.writeCSV()