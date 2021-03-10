import os
import shutil

def reconformFiles(pathSrc, pathDst):
    srcFile = pathSrc.rpartition(os.sep)[-1]
    srcFolder = pathSrc.rpartition(os.sep)[0]
    listExt = ["exr", "dpx", "cin", "png", "jpg", "tif", "tiff", "jpeg", "psd"]

    if not srcFile.rpartition(".")[-1] in listExt:
        """ singl file """
        if not os.path.exists(pathDst):
            os.makedirs(pathDst)
        if not os.path.exists(pathDst + os.sep + srcFile):
            shutil.copy2(srcFolder + os.sep + srcFile, pathDst + os.sep + srcFile)

    else:
        if not os.path.exists(pathDst):
            os.makedirs(pathDst)
        if not os.path.exists(pathDst + os.sep + srcFile):
            shutil.copy2(srcFolder + os.sep + srcFile, pathDst + os.sep + srcFile)
            print(f"source      -----  {srcFolder}{os.sep}{srcFile}")
            print(f"destination -----  {pathDst}{os.sep}{srcFile}")

def fuScriptReconform():

    pathFuScript = os.getcwd()
    fuConform = ""
    str_in = "\"" + os.sep
    str_out = "\""
    pathSwitch = ""
    newLine = ""

    for fuScript in os.listdir(pathFuScript):
        if ".comp" in fuScript:
            fuComp = open(fuScript, "r")
            fuContent = fuComp.read()
            fuComp.close()
            shotPath = f"{pathFuScript}{os.sep}SHOTS{os.sep}{fuScript.rpartition('.comp')[0]}"
            if not os.path.exists(shotPath): os.makedirs(shotPath)

            for line in fuContent.splitlines():
                if "OutputClips" in line or "Saver" in line:
                    pathSwitch = "OUT"
                if "Loader" in line:
                    pathSwitch = "SRC"
                if "LastFile" in line:
                    pathSwitch = "NON"

                if str_in in line:
                    if pathSwitch == "OUT":
                        srcPath = os.sep + line.split(str_in)[1].split(str_out)[0]
                        srcFile = srcPath.split(os.sep)[-1]
                        destPath = f"{shotPath}{os.sep}IMAGES{os.sep}{pathSwitch}"
                        if not os.path.exists(destPath): os.makedirs(destPath)
                        newLine = line.replace(srcPath, f"Comp:{os.sep}..{os.sep}IMAGES{os.sep}{pathSwitch}{os.sep}v01{os.sep}{srcFile}")

                    if pathSwitch == "SRC":
                        srcPath = os.sep + line.split(str_in)[1].split(str_out)[0]
                        srcFile = srcPath.split(os.sep)[-1]
                        destFile = f"{shotPath}{os.sep}IMAGES{os.sep}{pathSwitch}"
                        if not os.path.exists(destFile): os.makedirs(destFile)
                        newLine = line.replace(srcPath, f"Comp:{os.sep}..{os.sep}IMAGES{os.sep}{pathSwitch}{os.sep}{srcFile}")
                        if os.path.exists(srcPath.rpartition(os.sep)[0] + os.sep):
                            reconformFiles(srcPath.rpartition(os.sep)[0] + os.sep + srcFile, destFile)

                            print(newLine)
                            print(f"\n\n")
                            # print(destFile)
                        else:
                            print("no exist")

                    if pathSwitch == "NON":
                        srcPath = os.sep + line.split(str_in)[1].split(str_out)[0]
                        newLine = line.replace(srcPath,"")

                else:
                    newLine = line
                fuConform += newLine + "\n"
            # print(fuConform)
            fuComp = f"{fuScript.rpartition('.')[0]}_v01.comp"
            scriptPath = f"{shotPath}{os.sep}SCRIPTS"
            print(f"\n\n{fuComp}\n\n\n\n")
            if not os.path.exists(scriptPath): os.makedirs(scriptPath)
            newFuScript = open(f"{scriptPath}{os.sep}{fuComp}", "w+")
            newFuScript.write(fuConform)
            newFuScript.close()


fuScriptReconform()
