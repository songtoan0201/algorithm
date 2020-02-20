String findProfession(int level, int pos) {
    if(level==1) return "Engineer";

    String p = findProfession(level - 1, (int) Math.floor((pos + 1)/2));
    // 1
    if(p == "Engineer") {
        return (pos % 2) == 1 ? "Engineer" : "Doctor";
    }
    else if(p == "Doctor") {
        return (pos % 2) == 1 ? "Doctor" : "Engineer";
    }
    return "";
}
