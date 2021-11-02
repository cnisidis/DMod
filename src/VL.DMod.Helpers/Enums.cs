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

    public enum DSegmentPlacement
    {
        None,//δαπέδου
        W //επιτοίχειο

    }
        


    public enum DSegmentType
    {
        R,  //only R
        RE, //R extended
        C, //
        U01 //πόδι για ντουλάπι
    }
}
