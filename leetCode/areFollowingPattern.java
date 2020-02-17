boolean areFollowingPatterns(String[] strings, String[] patterns) {
    HashSet set1 = new HashSet();
    HashSet set2 = new HashSet();
    for(int i=0; i<strings.length;i++){
        boolean added = set1.add(strings[i]);  
        boolean added1 = set2.add(patterns[i]);
        System.out.println(added);
        System.out.println(added1);
        if(added != added1){
            return false;
        }
    }
    return true;
}
