import subprocess
import os

class RulesCalled(object,):
    def __init__(self, pathTowrite):
        self.pathTowrite = pathTowrite

    # Information written in the command Prompt and saved in a txt file
    def writeRule(self,command,nameFile):
        lpFile = open(self.pathTowrite + nameFile, 'w')
        subprocess.call("(cd D:\Diego\MASTER\Master Thesis\Clingon\clingo-5.2.1-win64 && " + command + ")", shell=True, stdout=lpFile)
        lpFile.close()

    # Call each ASP file depending of the information given
    def eachRule(self, ruleID,solution,*args):
        if not solution:
            ASPmainFile = open("D:\\Diego\\MASTER\\Master Thesis\\Clingon\\clingo-5.2.1-win64\\usecase1V1.1Temp.lp",'r')
        elif solution == "main":
            ASPmainFile = open("D:\\Diego\\MASTER\\Master Thesis\\Clingon\\clingo-5.2.1-win64\\solutions.lp",'r')
        elif solution == "individual":
            ASPmainFile = open("D:\\Diego\\MASTER\\Master Thesis\\Clingon\\clingo-5.2.1-win64\\solutionsIndividual.lp",'r')
        file = ASPmainFile.readlines()
        TempText = ""
        startIndex = 0
        index = 0
        ruleID = ruleID
        if len(args) > 0 and os.stat("D:\\Diego\\MASTER\\Master Thesis\\Clingon\\clingo-5.2.1-win64\\" + args[0]).st_size == 0:
            print("Empty file")
            return
        else:
            for i in file:
                if i == '\n':
                    TempText = self.writefileRule(startIndex,index,file,TempText,ruleID)
                    if len(TempText) > 20:
                        lpFile = open("D:\\Diego\\MASTER\\Master Thesis\\Clingon\\clingo-5.2.1-win64\\TempRule.lp", 'w')
                        lpFile.write(TempText)
                        lpFile.close()
                        if len(args) == 0:
                            command = "clingo-python.exe Rules.lp helperRules.lp  TempRule.lp " \
                                      "python_functions.lp linesTrenchTwenteMedium2.lp circleTwenteMedium2.lp otherUtilitiesTwenteMedium2.lp  " \
                                      "parametersTrenchTwenteMedium2.lp soilCharacteristicsMedium2.lp polygonTwenteMedium2.lp linesVehicleSegmentMedium2.lp  " \
                                      "parametersOtherPipesTwenteMedium2.lp polygonEquipment_areas.lp polygonPiled_soil_areas.lp RulesConstrain.lp  combinationsMainNetwork.lp " \
                                      "combinationsIndividualNetwork.lp "
                        else:
                            command = "clingo-python.exe Rules.lp helperRules.lp  TempRule.lp " \
                                      "python_functions.lp linesTrenchTwenteMedium2.lp circleTwenteMedium2.lp otherUtilitiesTwenteMedium2.lp  " \
                                      "soilCharacteristicsMedium2.lp polygonTwenteMedium2.lp linesVehicleSegmentMedium2.lp  " \
                                      "parametersOtherPipesTwenteMedium2.lp polygonEquipment_areas.lp polygonPiled_soil_areas.lp RulesConstrain.lp  " \
                                      "combinationsMainNetwork.lp combinationsIndividualNetwork.lp  " + args[0]
                        self.writeRule(command,"file" + str(ruleID) + ".txt")
                        print("File rule output " + str(ruleID) + " written")
                        ruleID += 1

                    elif TempText != "False":
                        if len(args) == 0:
                            command = "clingo-python.exe Rules.lp helperRules.lp  " \
                                      "python_functions.lp linesTrenchTwenteMedium2.lp circleTwenteMedium2.lp otherUtilitiesTwenteMedium2.lp  " \
                                      "parametersTrenchTwenteMedium2.lp soilCharacteristicsMedium2.lp polygonTwenteMedium2.lp linesVehicleSegmentMedium2.lp " \
                                      "parametersOtherPipesTwenteMedium2.lp polygonEquipment_areas.lp polygonPiled_soil_areas.lp RulesConstrain.lp  combinationsMainNetwork.lp  " \
                                      "combinationsIndividualNetwork.lp  " + TempText
                        else:
                            command = "clingo-python.exe Rules.lp helperRules.lp  " \
                                      "python_functions.lp linesTrenchTwenteMedium2.lp circleTwenteMedium2.lp otherUtilitiesTwenteMedium2.lp  " \
                                       + args[0] + "soilCharacteristicsMedium2.lp polygonTwenteMedium2.lp linesVehicleSegmentMedium2.lp " \
                                      "parametersOtherPipesTwenteMedium2.lp polygonEquipment_areas.lp polygonPiled_soil_areas.lp RulesConstrain.lp  combinationsMainNetwork.lp  " \
                                                   "combinationsIndividualNetwork.lp  " + TempText
                        self.writeRule(command,"file" + str(ruleID) + ".txt")
                        print("File rule output " + str(ruleID) + " written" )
                        ruleID += 1
                    TempText = ""
                    startIndex = index + 1

                index += 1

    # ASP files written in different format that should be called by name
    def writefileRule(self,start,end,file,TempText,ruleID):
        rulesArray = ["rule12","rule13","rule21","rule22","rule23","rule24","rule25","rule26","rule27","rule28","rule30","rule31",
                      "rule32","rule33"]
        for eachRule in rulesArray:
            if eachRule in file[start]:
                RuleCompesed = True
                break
            else:
                RuleCompesed = False

        if RuleCompesed == True:

            arr = os.listdir("D:\\Diego\\MASTER\\Master Thesis\\Clingon\\clingo-5.2.1-win64\\")

            ruleName = eachRule

            for i in arr:
                if i == ruleName + ".lp":
                    return(i)
            return("False")

        else:
            while start <= end:
                TempText = TempText + file[start]
                start += 1
            return(TempText)


