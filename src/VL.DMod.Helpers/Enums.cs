using System;
using System.Collections.Generic;

namespace VL.DMod.Helpers
{
    public enum DTileArrangement
    {
        START,
        MIDDLE,
        END
    }

    public enum DModuleType
    {
        R1,
        R2,
        R3,
        R4,
        C0,
        C1,
        C2,
        C3,
        C4,
        S0 //space
    }

    public enum DModulePlacement
    {

        B,//Base
        W //επιτοίχειο

    }
        

    public enum DSegmentType
    {
        
        U, //μεταλλικός (κοινός) ορθοστάτης
        UC, // μεταλλικός κοινός ορθοστάτης για ντουλάπια
        UR, //μεταλλικός ορθοστάτης με ράφι στο τελείωμα
        UW, //ορθοστάτες τοίχου
        UWC, //ορθοστάτες τοίχου για ντουλάπια
        UWR //ορθοστάτες τοίχου με ράφι στο τελείωμα
    }

    public enum DModAppStates
    {
        EDITING,
        SAVING,
        LOADING,
        DRAWING,
        SENDING

    }

    public enum DModFunctionality
    {
        TILES,
        SKETCH
    }

    public enum DModInteractionArea
    {

    }

    public enum DModAppContext
    {
        GRID,
        EDITMODULE,
        EDITTILE,
        PICKMODULE,
        DELETEMODULE,
        SAVEDIALOG,
        IMPORTDIALOG,
        LOADDIALOG 
    }

    public class DModEnums
    {
        public DModEnums()
        {

        }
        public static string[] GetNames(object obj)
        {
            List<string> names = new List<string>();
            foreach (string name in Enum.GetNames(typeof(object)))
            {
                names.Add(name);
            }
            return names.ToArray();
        }

        public static string[] GetDModuleTypeNames()
        {
            List<string> names = new List<string>();
            foreach (string name in Enum.GetNames(typeof(DModuleType)))
            {
                names.Add(name);
            }
            return names.ToArray();
        }
    }

    
    
}
