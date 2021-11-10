using System;

namespace VL.DMod.Helpers
{
    public enum DModuleType
    {
        R1,
        R2,
        R3,
        R4,
        C1,
        C2,
        C3,
        C4
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

    
}
