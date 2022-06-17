class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        ListNode myNode = new ListNode();
        int minNodeIndex = 0;
        int nodeNullCount = 0;
        int minNodeValue;
       
        while(nodeNullCount < lists.length){
            for(int i = 0; i < lists.length; i++){
                if(lists[i] != null){
                    System.out.println(lists[i].val);
                    lists[i] = lists[i].next;
                }else{
                    // nodeNullCount += 1;
                    continue;
                }
            }
            nodeNullCount += 1;
        }
        
        // System.out.println(lists[0].val);
        // System.out.println(lists[0].next.val);
        // System.out.println(lists[0].next.next.val);
        
        ListNode node = new ListNode();
        return node;
    }
}