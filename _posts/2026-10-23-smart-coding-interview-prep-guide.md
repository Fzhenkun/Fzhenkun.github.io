---
title: 面试刷题速刷总表 SMART 版本
date: 2026-10-23 12:00:00 +0800
categories: [算法, 面试]
tags: [algorithm, coding-interview, cpp]
published: true
---

> 目标：把目录中的零散题解压缩成 12 个高频模型。首轮先掌握“看到什么信号就想到什么模板”，再用限时手撕和错题复写验证，而不是背 40 多段代码。

## 一、SMART 总目标

| 维度 | 目标 |
|---|---|
| S 具体 | 完成用户指定的 P0/P1/P2 共 12 个主题，覆盖数组、哈希、双指针、链表、栈、树、DP、排序、堆、回溯、矩阵、贪心、二分等面试高频模型。 |
| M 可度量 | 首轮完成 45 个代表题；P0 每题连续两次在 20 分钟内独立写出并能讲清复杂度；P1 在 25 分钟内完成；P2 能说清状态/不变量和边界。 |
| A 可实现 | 每次只攻一个模型，按“理解 10 分钟、限时编码 20 分钟、复盘 10 分钟”执行；卡住 10 分钟先写暴力，再看提示。 |
| R 相关 | 题目均服务于面试手撕：识别模型、解释取舍、写出可运行代码、自测边界、报告复杂度。 |
| T 有期限 | 建议 10 天完成首轮，随后按 D+1、D+3、D+7 复写错题；面试前 2 天只做随机抽题和口述。 |

### 首轮完成标准

- [ ] 每个主题都能脱稿写出至少一个通用模板。
- [ ] 每道题都记录“识别信号、核心不变量/状态、复杂度、一个最容易错的边界”。
- [ ] P0 题不依赖题解完成两次；P1 题至少一次独立完成；P2 题能在白板上推导。
- [ ] 随机抽 4 题，连续 90 分钟内完成至少 3 题，并能逐题口述思路。

## 二、题目范围与优先级

| 优先级 | 模块 | 必刷代表题 | 面试价值 |
|---|---|---|---|
| P0 | 数组与哈希 | 两数之和、和为 K 的子数组、缺失的第一个正数、旋转数组、除自身以外数组的乘积 | 哈希、前缀和、原地标记的基础分水岭 |
| P0 | 双指针与滑动窗口 | 合并有序数组、三数之和、盛最多水、接雨水、无重复字符最长子串、字母异位词 | 高频线性扫描模型，容易被追问不变量 |
| P0 | 链表 | 反转、相交、环入口、回文、K 个一组翻转、LRU | 指针安全、快慢指针、哈希加双向链表 |
| P0 | 栈与单调栈 | 最小栈、字符串解码、每日温度、柱状图最大矩形 | 处理嵌套结构、下一个更大/更小、边界哨兵 |
| P0 | 二叉树基础 | DFS/BFS、中序第 K 小、路径和、遍历构造二叉树、右视图 | 递归定义、层序遍历、BST 性质 |
| P0 | 动态规划基础 | 打家劫舍、零钱兑换、完全平方数、LIS、最小路径和、LCS | 状态定义、转移、初始化、遍历顺序 |
| P1 | 排序与堆 | 快排、归并、堆、Top K、数据流中位数 | 手写排序和动态维护最值 |
| P1 | 回溯与矩阵 | 括号生成、单词搜索、矩阵置零、螺旋矩阵、旋转图像 | 状态恢复、原地标记、边界收缩 |
| P1 | 贪心与技巧 | 买卖股票、异或、摩尔投票、颜色分类、下一个排列 | 证明局部选择，掌握位运算与原地技巧 |
| P2 | DP 进阶 | 乘积最大子数组、最长回文子串、编辑距离、最长有效括号、单词拆分 | 多状态、区间 DP、字符串 DP |
| P2 | 二分与综合变式 | 搜索二维矩阵、排序边界、答案二分 | 把“找位置”统一为单调判定 |


**刷题顺序**：先刷链表和数组/双指针的 `P0` 题，形成指针、哈希和窗口模板；再刷树、DP 和栈；最后用堆、回溯、贪心、二分补齐变式。每道题记录牛客题号、识别信号、核心不变量、复杂度和一个边界用例。

| 补充 | 牛客 Hot 101 去重新增 | 链表区间/合并/删除、二分边界、树遍历与性质、栈队列、回溯、DP、字符串、贪心、模拟 | 补齐题库覆盖；每道题均在第五部分给出关键注释代码 |

## 三、面试手撕通用流程

1. **读约束**：确认输入规模、是否有序、是否允许修改、重复值、负数、空输入和返回形式。
2. **说暴力**：先给出直接解法及复杂度，再指出重复计算或无效枚举在哪里。
3. **认模型**：在哈希、排序、双指针、窗口、栈、堆、前缀和、DFS/BFS、DP、二分中选一个，并说出理由。
4. **定不变量**：循环每次开始时什么成立？栈中保存什么？`dp[i]` 代表什么？
5. **编码**：先写主流程，再补边界；链表先保存 `next`，原地题先保护标记信息。
6. **自测**：至少检查空/单元素、重复值、全相同、单调递增/递减、答案在首尾、负数或溢出。
7. **收尾**：说明时间、额外空间、替代方案和不能使用某方案的原因。

## 四、核心题型与速记

### P0-1 数组与哈希

- **识别信号**：查补数/查存在性想到哈希；连续区间和想到前缀和；要求 O(1) 额外空间且值域与下标相关想到原地标记；循环移动想到三次反转。
- **核心方法**：两数之和用 `target - x` 查表；和为 K 用 `prefix - k` 查前缀和频次；最长和为 K 只保留前缀和首次下标；缺失正数把 `1..n` 映射回数组下标；乘积数组用左右前缀乘积避免除法。
- **代表题**：两数之和、和为 K 的子数组、缺失的第一个正数、旋转数组、除自身以外数组的乘积。
- **易错点**：`freq[0] = 1` 与 `pos[0] = -1` 含义不同；两数之和要先查后存避免同一元素重复；旋转时 `m %= n`；乘积题不能用除法；原地标记要先处理非正数/越界值。
- **验收**：能解释“计数”和“首次位置”为什么使用不同 map；能在 O(n) 时间写出除自身乘积和最小缺失正数。


- **新增题目**：**新增**数组中只出现一次的两个数字。

### 新增题目代码（新增）

```cpp
// 新增：两个只出现一次的数字：整体异或得到 a^b，按最低不同位把数组分组。
vector<int> twoSingles(vector<int>& a){int x=0;for(int v:a)x^=v;int bit=x&-x,u=0,v=0;for(int z:a)(z&bit?u:v)^=z;return {u,v};}


```

### P0-2 双指针与滑动窗口

- **识别信号**：数组有序或排序后利用单调性，用左右指针；连续子串/子数组且窗口需要保持合法，用滑动窗口；“三数之和”通常排序后固定一个数，再用双指针。
- **核心不变量**：合并有序数组从后向前填充，避免覆盖；盛最多水每次移动较短边；接雨水可用左右最大值或单调栈；窗口扩张后只收缩到重新合法；异位词窗口维护字符计数。
- **代表题**：合并有序数组、三数之和、盛最多水、接雨水、无重复字符最长子串、字母异位词。
- **易错点**：三数之和三层去重；窗口左指针不能回退；接雨水边界高度不参与蓄水；合并数组从尾部写；指针移动必须由不变量解释，不能凭感觉。
- **验收**：能在 3 分钟说清窗口含义、扩张条件、收缩条件和答案更新时机；三数之和能处理重复值。


- **新增题目**：**新增**合并区间、**新增**最小覆盖子串、**新增**反转字符串、**新增**最长无重复子数组、**新增**判断是否为回文字符串。

### 新增题目代码（新增）

```cpp
// 新增：字符串变形/反转：按单词边界收集后逆序；原地反转只需双指针交换。
string transform(string s){stringstream ss(s);vector<string>v;string w;while(ss>>w)v.push_back(w);reverse(v.begin(),v.end());string r;for(auto&x:v)r+=(r.empty()?"":" ")+x;return r;}
string reverseString(string s){reverse(s.begin(),s.end());return s;}

// 新增：最长公共前缀：不断缩短前缀，直到它成为每个字符串的前缀。
string commonPrefix(vector<string>&v){if(v.empty())return "";string p=v[0];for(int i=1;i<v.size();++i)while(v[i].find(p)!=0)p.pop_back();return p;}

// 新增：IP 校验：按点切段，检查非空、无前导零、数值范围；IPv6 每段 1..4 个十六进制字符。
bool validIPv4(string s){stringstream ss(s);string x;int cnt=0;while(getline(ss,x,'.')){if(x.empty()||(x.size()>1&&x[0]=='0')||x.size()>3||!all_of(x.begin(),x.end(),::isdigit)||stoi(x)>255)return false;++cnt;}return cnt==4;}

// 新增：大数加法：从末位向前模拟进位，避免依赖整型范围。
string addBig(string a,string b){string r;int i=a.size()-1,j=b.size()-1,c=0;while(i>=0||j>=0||c){int s=c+(i>=0?a[i--]-'0':0)+(j>=0?b[j--]-'0':0);r.push_back('0'+s%10);c=s/10;}reverse(r.begin(),r.end());return r;}

// 新增：回文字符串/最长无重复子数组：前者向内收缩，后者维护窗口内每个值的最近位置。
bool palindromeString(string s){int l=0,r=s.size()-1;while(l<r)if(s[l++]!=s[r--])return false;return true;}
int longestUniqueArray(vector<int>&a){unordered_map<int,int>last;int l=0,ans=0;for(int r=0;r<a.size();++r){if(last.count(a[r]))l=max(l,last[a[r]]+1);last[a[r]]=r;ans=max(ans,r-l+1);}return ans;}

// 新增：合并区间：先按左端点排序，当前区间能覆盖到就扩展，否则输出并开启新区间。
vector<vector<int>> mergeIntervals(vector<vector<int>>&a){sort(a.begin(),a.end());vector<vector<int>>r;for(auto x:a)if(r.empty()||r.back()[1]<x[0])r.push_back(x);else r.back()[1]=max(r.back()[1],x[1]);return r;}

// 新增：最小覆盖子串：need 满足后收缩左端，记录最短合法窗口。
string minWindow(string s,string t){unordered_map<char,int>need;for(char c:t)need[c]++;int miss=t.size(),l=0,beg=0,len=INT_MAX;for(int r=0;r<s.size();++r){if(need[s[r]]-->0)--miss;while(!miss){if(r-l+1<len)len=r-l+1,beg=l;if(++need[s[l++]]>0)++miss;}}return len==INT_MAX?"":s.substr(beg,len);}


```

### P0-3 链表

- **识别信号**：需要改变头节点先用虚拟头；需要找中点/环入口用快慢指针；判断相交比较节点地址而不是节点值；需要 O(1) 查询和淘汰顺序用哈希表 + 双向链表。
- **核心模板**：反转时保存 `next` 再改 `cur->next`；回文先找中点、反转后半段、逐节点比较；K 个一组先确认剩余节点数，再翻转区间；环入口用相遇后把一个指针放回头部；LRU 中 map 存迭代器/节点地址，双向链表头部表示最近使用。
- **代表题**：反转链表、相交链表、环形链表 II、回文链表、K 个一组翻转链表、LRU 缓存。
- **易错点**：翻转时丢失后继；分组不足 K 个时不能翻转；相交判断是地址相同；删除节点要同时改前后指针；LRU 的 `get` 也必须更新新鲜度。
- **验收**：不看资料写出反转、虚拟头、快慢指针和 LRU 的四个关键操作，并能说明空间复杂度。


- **新增题目**：**新增**链表内指定区间反转、**新增**合并两个排序的链表、**新增**合并 k 个已排序的链表、**新增**判断链表中是否有环、**新增**链表中倒数最后 k 个结点、**新增**删除链表的倒数第 n 个节点、**新增**链表相加（二）、**新增**单链表的排序、**新增**链表的奇偶重排、**新增**删除有序链表中重复的元素-I、**新增**删除有序链表中重复的元素-II。

### 新增题目代码（新增）

```cpp
// 新增：链表区间反转：先用虚拟头统一处理 left=1，再把区间节点逐个头插到前驱之后。
ListNode* reverseBetween(ListNode* head, int left, int right) {
    ListNode dummy(0, head), *pre = &dummy;
    for (int i = 1; i < left; ++i) pre = pre->next;
    ListNode* cur = pre->next;
    for (int i = left; i < right; ++i) {
        ListNode* move = cur->next; cur->next = move->next;
        move->next = pre->next; pre->next = move;
    }
    return dummy.next;
}

// 新增：合并两个有序链表：每次摘取较小节点，剩余链表直接接到尾部。
ListNode* mergeTwo(ListNode* a, ListNode* b) {
    ListNode dummy(0); ListNode* tail = &dummy;
    while (a && b) { if (a->val <= b->val) tail->next = a, a = a->next;
                     else tail->next = b, b = b->next; tail = tail->next; }
    tail->next = a ? a : b; return dummy.next;
}

// 新增：合并 k 个链表：小根堆只保存每条链当前最小节点，空间为 k。
ListNode* mergeK(vector<ListNode*>& lists) {
    priority_queue<ListNode*, vector<ListNode*>, Cmp> pq;
    for (auto p : lists) if (p) pq.push(p);
    ListNode dummy(0); ListNode* tail = &dummy;
    while (!pq.empty()) { auto p = pq.top(); pq.pop(); tail->next = p; tail = p;
                           if (p->next) pq.push(p->next); }
    return dummy.next;
}

// 新增：环检测：快指针每次走两步，能相遇说明存在环。
bool hasCycle(ListNode* head) {
    ListNode *slow = head, *fast = head;
    while (fast && fast->next) { slow = slow->next; fast = fast->next->next;
                                 if (slow == fast) return true; }
    return false;
}

// 新增：倒数第 k 个：先让 fast 领先 k 步，slow 到达目标前驱/目标位置。
ListNode* kthFromEnd(ListNode* head, int k) {
    ListNode *fast = head, *slow = head;
    while (k-- && fast) fast = fast->next;
    while (fast) fast = fast->next, slow = slow->next;
    return slow;
}

// 新增：删除倒数第 n 个：虚拟头使删除头节点与普通节点走同一套逻辑。
ListNode* removeNthFromEnd(ListNode* head, int n) {
    ListNode dummy(0, head), *fast = &dummy, *slow = &dummy;
    for (int i = 0; i < n; ++i) fast = fast->next;
    while (fast->next) fast = fast->next, slow = slow->next;
    slow->next = slow->next->next; return dummy.next;
}

// 新增：链表相加：按位相加并携带 carry，输入链表本身不反转。
ListNode* addLists(ListNode* a, ListNode* b) {
    ListNode dummy(0); ListNode* tail = &dummy; int carry = 0;
    while (a || b || carry) { int s = carry + (a ? a->val : 0) + (b ? b->val : 0);
        tail->next = new ListNode(s % 10); carry = s / 10; tail = tail->next;
        if (a) a = a->next; if (b) b = b->next; }
    return dummy.next;
}

// 新增：链表排序：归并按中点拆分，递归深度 O(log n)，总时间 O(n log n)。
ListNode* sortList(ListNode* head) {
    if (!head || !head->next) return head;
    ListNode *slow = head, *fast = head->next;
    while (fast && fast->next) slow = slow->next, fast = fast->next->next;
    ListNode* right = slow->next; slow->next = nullptr;
    return mergeTwo(sortList(head), sortList(right));
}

// 新增：奇偶重排：odd/even 分别维护两条链，最后拼接；保持各自相对顺序。
ListNode* oddEvenList(ListNode* head) {
    if (!head) return head; ListNode *odd = head, *even = head->next, *eh = even;
    while (even && even->next) { odd->next = even->next; odd = odd->next;
        even->next = odd->next; even = even->next; }
    odd->next = eh; return head;
}

// 新增：有序链表去重 I/II：I 保留一个，II 对重复值整段删除。
ListNode* deleteDupKeep(ListNode* head) {
    for (auto p = head; p && p->next; ) if (p->val == p->next->val) p->next = p->next->next;
        else p = p->next; return head;
}
ListNode* deleteDupAll(ListNode* head) {
    ListNode dummy(0, head), *pre = &dummy;
    while (pre->next) { auto p = pre->next; while (p->next && p->next->val == p->val) p = p->next;
        if (p != pre->next) pre->next = p->next; else pre = pre->next; }
    return dummy.next;
}


```

### P0-4 栈与单调栈

- **识别信号**：括号/字符串嵌套用栈；需要右侧第一个更大/更小元素用单调栈；柱状图面积需要同时确定左右边界。
- **核心不变量**：栈中存下标而非值，才能计算距离/宽度；每日温度用单调递减栈，当前更高温度触发出栈；柱状图用递增栈，出栈时当前下标是右边界，新栈顶是左边界；最小栈用辅助栈同步记录每层最小值。
- **代表题**：最小栈、字符串解码、每日温度、柱状图最大矩形。
- **易错点**：连续出栈必须用 `while`；相等高度的处理规则要统一；柱状图首尾加 0 哨兵；解码 `]` 时要先恢复字符串再恢复倍数。
- **验收**：能解释每个元素最多入栈/出栈一次，因此是 O(n)；能手推柱状图 `[2,1,5,6,2,3]` 的边界。


- **新增题目**：**新增**用两个栈实现队列、**新增**有效括号序列、**新增**滑动窗口的最大值、**新增**最小的 K 个数、**新增**表达式求值。

### 新增题目代码（新增）

```cpp
// 新增：两栈队列：输入栈负责入队，输出栈为空时整体倒序搬运，摊销 O(1)。
class TwoStackQueue { stack<int> in,out; public: void push(int x){in.push(x);} int pop(){if(out.empty())while(!in.empty())out.push(in.top()),in.pop();int x=out.top();out.pop();return x;} };

// 新增：有效括号：栈顶必须匹配当前右括号，最后栈必须为空。
bool validBrackets(string s) { stack<char> st; for(char c:s){if(c=='('||c=='['||c=='{')st.push(c);else{if(st.empty()||(c==')'&&st.top()!='(')||(c==']'&&st.top()!='[')||(c=='}'&&st.top()!='{'))return false;st.pop();}}return st.empty(); }

// 新增：滑动窗口最大值：单调递减双端队列保存候选下标，队首永远是窗口最大值。
vector<int> maxWindow(vector<int>& a,int k){deque<int> q;vector<int>ans;for(int i=0;i<a.size();++i){while(!q.empty()&&q.front()<=i-k)q.pop_front();while(!q.empty()&&a[q.back()]<=a[i])q.pop_back();q.push_back(i);if(i>=k-1)ans.push_back(a[q.front()]);}return ans;}

// 新增：最小 K 个数：大根堆只保留 K 个最小候选，堆顶是当前最大值。
vector<int> smallestK(vector<int>& a,int k){priority_queue<int>q;for(int x:a){q.push(x);if(q.size()>k)q.pop();}vector<int>ans;while(!q.empty())ans.push_back(q.top()),q.pop();return ans;}

// 新增：表达式求值：数字入栈，遇到运算符结算上一个运算符，乘除优先在入栈前完成。
int calculate(string s){stack<int>st;long long num=0;char op='+';for(int i=0;i<=s.size();++i){if(i<s.size()&&isdigit(s[i]))num=num*10+s[i]-'0';else if(i==s.size()||s[i]!=' '){if(op=='+')st.push(num);else if(op=='-')st.push(-num);else{int x=st.top();st.pop();st.push(op=='*'?x*num:x/num);}num=0;if(i<s.size())op=s[i];}}int ans=0;while(!st.empty())ans+=st.top(),st.pop();return ans;}


```

### P0-5 二叉树基础

- **识别信号**：树题先问是节点值、深度、路径和还是路径列表；层级信息用 BFS；BST 的中序序列有序；前序第一个节点是根，中序用于切分左右子树。
- **核心模板**：DFS 先定义函数返回值、空节点返回值、当前节点动作、左右子树如何合并；BFS 用队列并记录每层节点数；路径和含负数时不能用“超过 target 就剪枝”；右视图可取每层最后一个，或 DFS 先右后左。
- **代表题**：DFS/BFS、中序第 K 小、路径和、前序与中序构造二叉树、二叉树右视图。
- **易错点**：`k` 和路径数组的传递方式；路径是否必须从根到叶；构造树不要反复切 vector，使用中序下标 map；空树和单节点。
- **验收**：能用递归和迭代各写一次遍历；能说明第 K 小为何只适用于 BST；能处理负数路径和。


- **新增题目**：**新增**二叉树的前序遍历、**新增**二叉树的中序遍历、**新增**二叉树的后序遍历、**新增**求二叉树的层序遍历、**新增**按之字形顺序打印二叉树、**新增**二叉树的最大深度、**新增**二叉搜索树与双向链表、**新增**对称的二叉树、**新增**合并二叉树、**新增**二叉树的镜像、**新增**判断是不是二叉搜索树、**新增**判断是不是完全二叉树、**新增**判断是不是平衡二叉树、**新增**二叉搜索树的最近公共祖先、**新增**在二叉树中找到两个节点的最近公共祖先、**新增**序列化二叉树。

### 新增题目代码（新增）

```cpp
// 新增：二叉树三种遍历：用统一的显式栈模拟递归，栈中保存待处理节点。
void preorder(TreeNode* root, vector<int>& out) { if(!root)return; out.push_back(root->val); preorder(root->left,out); preorder(root->right,out); }
void inorder(TreeNode* root, vector<int>& out) { if(!root)return; inorder(root->left,out); out.push_back(root->val); inorder(root->right,out); }
void postorder(TreeNode* root, vector<int>& out) { if(!root)return; postorder(root->left,out); postorder(root->right,out); out.push_back(root->val); }

// 新增：层序遍历：每轮固定当前队列长度，天然得到一层结果。
vector<vector<int>> levelOrder(TreeNode* root) {
    vector<vector<int>> ans; if(!root)return ans; queue<TreeNode*> q; q.push(root);
    while(!q.empty()){ int n=q.size(); vector<int> row; while(n--){auto p=q.front();q.pop();row.push_back(p->val);if(p->left)q.push(p->left);if(p->right)q.push(p->right);} ans.push_back(row); } return ans;
}

// 新增：之字形：按层方向写入，或统一层序后反转偶数层。
vector<vector<int>> zigzag(TreeNode* root) { auto ans=levelOrder(root); for(int i=1;i<ans.size();i+=2) reverse(ans[i].begin(),ans[i].end()); return ans; }

// 新增：树高：空树为 0，当前高度是左右子树较大值加一。
int maxDepth(TreeNode* root) { return root ? 1 + max(maxDepth(root->left), maxDepth(root->right)) : 0; }

// 新增：BST 转双向链表：中序遍历顺序就是升序，prev 连接当前节点。
TreeNode* bstToList(TreeNode* root) { TreeNode *head=nullptr,*prev=nullptr; function<void(TreeNode*)> dfs=[&](TreeNode* p){if(!p)return;dfs(p->left);if(prev)prev->right=p;else head=p;p->left=prev;prev=p;dfs(p->right);}; dfs(root); return head; }

// 新增：对称树：同时比较两棵镜像子树的外侧和内侧节点。
bool mirror(TreeNode* a, TreeNode* b) { if(!a||!b)return a==b; return a->val==b->val&&mirror(a->left,b->right)&&mirror(a->right,b->left); }
bool isSymmetric(TreeNode* root) { return !root || mirror(root->left,root->right); }

// 新增：合并树/镜像：递归复用一棵节点，空节点直接返回另一侧。
TreeNode* mergeTrees(TreeNode* a, TreeNode* b) { if(!a)return b;if(!b)return a;a->val+=b->val;a->left=mergeTrees(a->left,b->left);a->right=mergeTrees(a->right,b->right);return a; }
void invert(TreeNode* root) { if(!root)return; swap(root->left,root->right); invert(root->left); invert(root->right); }

// 新增：BST/完全树/平衡树：分别维护中序递增、层序空位规则和子树高度。
bool isBST(TreeNode* root, long long lo=LLONG_MIN, long long hi=LLONG_MAX) { if(!root)return true; return lo<root->val&&root->val<hi&&isBST(root->left,lo,root->val)&&isBST(root->right,root->val,hi); }
bool isComplete(TreeNode* root) { queue<TreeNode*>q;if(root)q.push(root);bool seenNull=false;while(!q.empty()){auto p=q.front();q.pop();if(!p){seenNull=true;continue;}if(seenNull)return false;q.push(p->left);q.push(p->right);}return true; }
int height(TreeNode* p) { if(!p)return 0;int l=height(p->left),r=height(p->right);if(l<0||r<0||abs(l-r)>1)return -1;return max(l,r)+1; }
bool balanced(TreeNode* root) { return height(root)>=0; }

// 新增：LCA：BST 利用大小关系；普通二叉树返回左右子树命中情况。
TreeNode* lcaBST(TreeNode* r, TreeNode* a, TreeNode* b) { while(r){if(a->val<r->val&&b->val<r->val)r=r->left;else if(a->val>r->val&&b->val>r->val)r=r->right;else return r;}return nullptr; }
TreeNode* lca(TreeNode* r, TreeNode* a, TreeNode* b) { if(!r||r==a||r==b)return r;auto l=lca(r->left,a,b),q=lca(r->right,a,b);return l&&q?r:l?l:q; }

// 新增：序列化：空指针也写入占位符，反序列化才能保留树结构而不产生歧义。
void serialize(TreeNode* r, string& s) { if(!r){s+="#,";return;}s+=to_string(r->val)+',';serialize(r->left,s);serialize(r->right,s); }
TreeNode* deserialize(queue<string>& q) { string x=q.front();q.pop();if(x=="#")return nullptr;TreeNode* r=new TreeNode(stoi(x));r->left=deserialize(q);r->right=deserialize(q);return r; }


```

### P0-6 动态规划基础

先写五句话：`dp` 定义、最后一步、转移方程、初始化、遍历顺序。不可达状态不要初始化成 0，避免把“不可能”当成可达。

| 题型 | 代表题 | 状态/关键点 | 复杂度 |
|---|---|---|---|
| 相邻不能同时选 | 打家劫舍 | `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`，可滚动 | O(n), O(1) |
| 完全背包/最少数量 | 零钱兑换、完全平方数 | `dp[0]=0`，其余设为不可达；每个状态尝试最后一个物品 | O(n·m) |
| 子序列 | LIS、LCS | LIS 明确严格递增；LCS 的公共子序列不要求连续 | O(n²) / O(mn) |
| 网格 | 最小路径和 | 由上方和左方转移，首行首列单独初始化 | O(mn) |
| 字符串可达 | 单词拆分 | `dp[i]` 表示前缀 `s[0..i)` 能否被拆分 | O(n²) 级别 |

- **易错点**：子数组/子串与子序列混淆；完全背包的遍历方向；`INT_MAX + 1` 溢出；空输入直接访问 `nums[0]`。
- **验收**：随机抽一题能在 5 分钟内写出状态和转移；至少一题能把 O(n) 空间优化到 O(1) 或 O(n)。


- **新增题目**：**新增**斐波那契数列、**新增**跳台阶、**新增**最小花费爬楼梯、**新增**最长公共子串、**新增**不同路径的数目（一）、**新增**把数字翻译成字符串、**新增**连续子数组的最大和、**新增**正则表达式匹配、**新增**打家劫舍（二）、**新增**买卖股票的最好时机（二）、**新增**买卖股票的最好时机（三）。

### 新增题目代码（新增）

```cpp
// 新增：斐波那契/跳台阶/爬楼梯：只保留前两项；爬楼梯的费用在踏上当前台阶时结算。
int fib(int n){int a=0,b=1;while(n--)a=b,b=a+b;return a;}
int climb(int n){int a=1,b=1;while(n--)a=b,b=a+b;return a;}
int minCost(vector<int>&c){int a=0,b=0;for(int i=2;i<=c.size();++i){int x=min(b+c[i-1],a+c[i-2]);a=b;b=x;}return b;}

// 新增：最长公共子串：必须连续，匹配时从 dp[i-1][j-1] 延伸，不匹配即清零。
int longestCommonSubstring(string a,string b){vector<int>dp(b.size()+1);int ans=0;for(int i=1;i<=a.size();++i)for(int j=b.size();j>=1;--j){dp[j]=a[i-1]==b[j-1]?dp[j-1]+1:0;ans=max(ans,dp[j]);}return ans;}

// 新增：不同路径：网格边界只有一条路径，其余来自上方与左方。
int uniquePaths(int m,int n){vector<int>dp(n,1);for(int i=1;i<m;++i)for(int j=1;j<n;++j)dp[j]+=dp[j-1];return dp[n-1];}

// 新增：数字翻译：dp[i] 表示前 i 位方案数，最近两位在 10..25 时可合并成一位。
int translateNum(string s){int a=1,b=1;for(int i=2;i<=s.size();++i){int two=stoi(s.substr(i-2,2));int c=b+(two>=10&&two<=25?a:0);a=b;b=c;}return b;}

// 新增：最大子数组和：dp 只关心以当前位置结尾的最优值，负前缀可直接舍弃。
int maxSubArray(vector<int>&a){int cur=a[0],ans=a[0];for(int i=1;i<a.size();++i)cur=max(a[i],cur+a[i]),ans=max(ans,cur);return ans;}

// 新增：正则匹配：* 可匹配零次或继续消耗，普通字符/点只从左上角转移。
bool regexMatch(string s,string p){int m=s.size(),n=p.size();vector<vector<bool>>dp(m+1,vector<bool>(n+1));dp[0][0]=true;for(int j=2;j<=n;++j)if(p[j-1]=='*')dp[0][j]=dp[0][j-2];for(int i=1;i<=m;++i)for(int j=1;j<=n;++j)if(p[j-1]=='*')dp[i][j]=dp[i][j-2]||((p[j-2]=='.'||p[j-2]==s[i-1])&&dp[i-1][j]);else dp[i][j]=(p[j-1]=='.'||p[j-1]==s[i-1])&&dp[i-1][j-1];return dp[m][n];}

// 新增：打家劫舍（二）：首尾不能同时取，分别计算 [0,n-2] 与 [1,n-1]。
int robRange(vector<int>&a,int l,int r){int x=0,y=0;for(int i=l;i<=r;++i){int z=max(y,x+a[i]);x=y;y=z;}return y;}
int robCircle(vector<int>&a){if(a.size()==1)return a[0];return max(robRange(a,0,a.size()-2),robRange(a,1,a.size()-1));}

// 新增：股票 II/III：II 累加所有上涨；III 用四个状态表示两次交易的持有/卖出。
int stockUnlimited(vector<int>&p){int ans=0;for(int i=1;i<p.size();++i)ans+=max(0,p[i]-p[i-1]);return ans;}
int stockTwo(vector<int>&p){int buy1=INT_MIN,sell1=0,buy2=INT_MIN,sell2=0;for(int x:p){buy1=max(buy1,-x);sell1=max(sell1,buy1+x);buy2=max(buy2,sell1-x);sell2=max(sell2,buy2+x);}return sell2;}


```

### P1-1 排序与堆

| 结构 | 识别信号 | 面试要点 | 复杂度 |
|---|---|---|---|
| 冒泡排序 | 需要用相邻交换逐步把极值移到边界 | 每轮把当前最大值推到末尾；加交换标记后已有序可提前结束，稳定、原地 | 最好 O(n)，平均/最坏 O(n²)，O(1) |
| 快速排序 | 需要原地分区 | pivot 分区后区间严格缩小；说明最坏 O(n²) 和随机 pivot | 平均 O(n log n) |
| 归并排序 | 需要稳定排序/归并 | 两个区间各自有序，耗尽一侧后追加另一侧 | O(n log n), O(n) |
| 堆 | 动态取最值、反复取当前最优 | C++ 默认大顶堆；插入/删除 O(log n) | 依题目而定 |
| Top K | 只保留 K 个候选 | 维护大小 K 的小顶堆，频次题先哈希统计 | O(n log K) |
| 数据流中位数 | 动态加入并查询中位数 | 大顶堆放较小一半，小顶堆放较大一半，大小差不超过 1 | 单次 O(log n) |

- **代表题**：快排、归并、堆、数组中的第 K 个最大元素、前 K 个高频元素、数据流中位数。
- **易错点**：第 K 大不是第 K 个不同值；比较器方向；中位数偶数个元素取两堆顶平均；快排全相同数据会退化。
- **验收**：能从零写快排分区、归并合并、大小 K 小顶堆；能解释为什么不必完整排序。


- **新增题目**：**新增**设计 LFU 缓存结构。

### 新增题目代码（新增）

```cpp
// 新增：LFU：频率升序链表/桶中维护最早访问节点，淘汰时先比频率再比时间。
class LFU { unordered_map<int,pair<int,int>> data; unordered_map<int,list<int>> bucket; int minFreq=0; public:
    int get(int k){if(!data.count(k))return -1;int v=data[k].first,f=data[k].second;bucket[f].remove(k);if(bucket[f].empty()&&minFreq==f)++minFreq;bucket[++f].push_front(k);data[k]={v,f};return v;}
};

```

### P1-2 回溯与矩阵

- **回溯四要素**：路径、选择列表、结束条件、剪枝；做选择、递归、撤销必须成对出现。
- **括号生成**：左括号数不超过 `n`，右括号数不超过左括号数；到长度 `2n` 收集答案。
- **单词搜索**：网格 DFS，访问时标记，返回后恢复；同一格不能在一次路径中重复使用。
- **矩阵置零**：用第一行/第一列做标记，但先记录它们原本是否含 0。
- **螺旋矩阵**：维护上下左右四个边界，每走完一条边立即判断是否越界。
- **旋转图像**：转置后逐行反转，或上下翻转后转置。
- **验收**：能说明每次递归返回后恢复了什么；矩阵题能在 O(1) 额外空间下处理首行首列为 0。


- **新增题目**：**新增**无重复项数字的全排列、**新增**有重复项数字的全排列、**新增**岛屿数量、**新增**字符串的排列、**新增**N 皇后问题、**新增**矩阵最长递增路径。

### 新增题目代码（新增）

```cpp
// 新增：全排列：交换当前位与后续位；有重复数字时用 set 跳过同层重复选择。
void permute(vector<int>& a,int i,vector<vector<int>>&ans){if(i==a.size()){ans.push_back(a);return;}unordered_set<int> used;for(int j=i;j<a.size();++j)if(used.insert(a[j]).second){swap(a[i],a[j]);permute(a,i+1,ans);swap(a[i],a[j]);}}

// 新增：字符串排列：同层用 set 去重，递归返回后撤销交换，保证每个分支从同一状态开始。
void permuteString(string& s,int i,vector<string>&ans){if(i==s.size()){ans.push_back(s);return;}unordered_set<char>used;for(int j=i;j<s.size();++j)if(used.insert(s[j]).second){swap(s[i],s[j]);permuteString(s,i+1,ans);swap(s[i],s[j]);}}

// 新增：岛屿数量：遇到陆地就 DFS 淹没整块，保证每个网格只访问一次。
void flood(vector<vector<char>>&g,int i,int j){if(i<0||j<0||i>=g.size()||j>=g[0].size()||g[i][j]!='1')return;g[i][j]='0';flood(g,i+1,j);flood(g,i-1,j);flood(g,i,j+1);flood(g,i,j-1);}
int islands(vector<vector<char>>&g){int ans=0;for(int i=0;i<g.size();++i)for(int j=0;j<g[0].size();++j)if(g[i][j]=='1')++ans,flood(g,i,j);return ans;}

// 新增：N 皇后：列、主对角线、次对角线分别记录已占用位置，冲突时剪枝。
void queens(int r,int n,vector<int>&usedCol,vector<int>&d1,vector<int>&d2,vector<int>&place,vector<vector<string>>&ans){if(r==n){vector<string>b(n,string(n,'.'));for(int i=0;i<n;++i)b[i][place[i]]='Q';ans.push_back(b);return;}for(int c=0;c<n;++c)if(!usedCol[c]&&!d1[r-c+n]&&!d2[r+c]){usedCol[c]=d1[r-c+n]=d2[r+c]=1;place[r]=c;queens(r+1,n,usedCol,d1,d2,place,ans);usedCol[c]=d1[r-c+n]=d2[r+c]=0;}}

// 新增：矩阵最长递增路径：记忆化 DFS，只有严格变大才转移。
int incDfs(vector<vector<int>>&a,int i,int j,vector<vector<int>>&memo){if(memo[i][j])return memo[i][j];int ans=1;int di[4]={1,-1,0,0},dj[4]={0,0,1,-1};for(int k=0;k<4;++k){int x=i+di[k],y=j+dj[k];if(x>=0&&y>=0&&x<a.size()&&y<a[0].size()&&a[x][y]>a[i][j])ans=max(ans,1+incDfs(a,x,y,memo));}return memo[i][j]=ans;}


```

### P1-3 贪心与技巧

| 题型 | 核心方法 | 必讲证明/边界 |
|---|---|---|
| 买卖股票 | 扫描维护历史最低买入价，更新最大收益 | 当前最低价之前的价格都不会更优；空数组/单日收益为 0 |
| 异或 | `x^x=0`、`x^0=x`，只出现一次的数异或全数组 | 两个只出现一次的数按最低不同位分组 |
| 摩尔投票 | 不同元素抵消，多数元素最终保留 | 题目必须保证多数元素存在，否则需二次验证 |
| 颜色分类 | 荷兰国旗三指针，维护 0 区、未处理区、2 区 | 交换 0 后当前位置前移，交换 2 后当前位置不能立即前移 |
| 下一个排列 | 找最长非增后缀，交换拐点与右侧刚好更大值，再反转后缀 | 全降序时整体反转；重复值要找“从右侧第一个更大” |

- **验收**：不能只说“每一步选最优”，要说局部选择排除了什么、为什么不损失全局最优、是否依赖排序或单调性。


- **新增题目**：**新增**字符串变形、**新增**最长公共前缀、**新增**验证 IP 地址、**新增**大数加法、**新增**分糖果问题、**新增**主持人调度（二）。

### 新增题目代码（新增）

```cpp
// 新增：字符串变形/反转：按单词边界收集后逆序；原地反转只需双指针交换。
string transform(string s){stringstream ss(s);vector<string>v;string w;while(ss>>w)v.push_back(w);reverse(v.begin(),v.end());string r;for(auto&x:v)r+=(r.empty()?"":" ")+x;return r;}
string reverseString(string s){reverse(s.begin(),s.end());return s;}

// 新增：最长公共前缀：不断缩短前缀，直到它成为每个字符串的前缀。
string commonPrefix(vector<string>&v){if(v.empty())return "";string p=v[0];for(int i=1;i<v.size();++i)while(v[i].find(p)!=0)p.pop_back();return p;}

// 新增：IP 校验：按点切段，检查非空、无前导零、数值范围；IPv6 每段 1..4 个十六进制字符。
bool validIPv4(string s){stringstream ss(s);string x;int cnt=0;while(getline(ss,x,'.')){if(x.empty()||(x.size()>1&&x[0]=='0')||x.size()>3||!all_of(x.begin(),x.end(),::isdigit)||stoi(x)>255)return false;++cnt;}return cnt==4;}

// 新增：大数加法：从末位向前模拟进位，避免依赖整型范围。
string addBig(string a,string b){string r;int i=a.size()-1,j=b.size()-1,c=0;while(i>=0||j>=0||c){int s=c+(i>=0?a[i--]-'0':0)+(j>=0?b[j--]-'0':0);r.push_back('0'+s%10);c=s/10;}reverse(r.begin(),r.end());return r;}

// 新增：回文字符串/最长无重复子数组：前者向内收缩，后者维护窗口内每个值的最近位置。
bool palindromeString(string s){int l=0,r=s.size()-1;while(l<r)if(s[l++]!=s[r--])return false;return true;}
int longestUniqueArray(vector<int>&a){unordered_map<int,int>last;int l=0,ans=0;for(int r=0;r<a.size();++r){if(last.count(a[r]))l=max(l,last[a[r]]+1);last[a[r]]=r;ans=max(ans,r-l+1);}return ans;}

// 新增：合并区间：先按左端点排序，当前区间能覆盖到就扩展，否则输出并开启新区间。
vector<vector<int>> mergeIntervals(vector<vector<int>>&a){sort(a.begin(),a.end());vector<vector<int>>r;for(auto x:a)if(r.empty()||r.back()[1]<x[0])r.push_back(x);else r.back()[1]=max(r.back()[1],x[1]);return r;}

// 新增：最小覆盖子串：need 满足后收缩左端，记录最短合法窗口。
string minWindow(string s,string t){unordered_map<char,int>need;for(char c:t)need[c]++;int miss=t.size(),l=0,beg=0,len=INT_MAX;for(int r=0;r<s.size();++r){if(need[s[r]]-->0)--miss;while(!miss){if(r-l+1<len)len=r-l+1,beg=l;if(++need[s[l++]]>0)++miss;}}return len==INT_MAX?"":s.substr(beg,len);}

// 新增：分糖果：左右各扫一次，取两个方向要求的较大值，保证相邻更高者糖果更多。
int candy(vector<int>&a){int n=a.size();vector<int>l(n,1),r(n,1);for(int i=1;i<n;++i)if(a[i]>a[i-1])l[i]=l[i-1]+1;for(int i=n-2;i>=0;--i)if(a[i]>a[i+1])r[i]=r[i+1]+1;int ans=0;for(int i=0;i<n;++i)ans+=max(l[i],r[i]);return ans;}

// 新增：主持人调度：按开始时间排序，用小根堆保存正在占用的最早结束时间。
int schedule(vector<vector<int>>&a){sort(a.begin(),a.end());priority_queue<int,vector<int>,greater<int>>q;for(auto&x:a){if(!q.empty()&&q.top()<=x[0])q.pop();q.push(x[1]);}return q.size();}


```

### P2-1 DP 进阶

| 题目 | 状态抓手 | 易错点 |
|---|---|---|
| 乘积最大子数组 | 同时维护当前最大值和最小值，负数会交换二者 | 不能只维护最大值；更新时先保存旧最大/最小 |
| 最长回文子串 | 区间 `dp[l][r]` 或中心扩展 | 区间长度顺序；子串必须连续 |
| 编辑距离 | `dp[i][j]` 表示前缀变换代价，插入/删除/替换取最小 | 下标含义和空前缀初始化 |
| 最长有效括号 | DP 或栈；DP 看前一段有效长度并找匹配左括号 | 越界检查；栈方案要放入哨兵下标 |
| 单词拆分 | 前缀可达 DP，枚举最后一个单词 | 字典单词可重复使用；不可达状态不能误判 |


- **新增题目**：**新增**正则表达式匹配、**新增**打家劫舍（二）、**新增**买卖股票的最好时机（二）、**新增**买卖股票的最好时机（三）。

### 新增题目代码（新增）

```cpp
// 新增：正则匹配：* 可匹配零次或继续消耗，普通字符/点只从左上角转移。
bool regexMatch(string s,string p){int m=s.size(),n=p.size();vector<vector<bool>>dp(m+1,vector<bool>(n+1));dp[0][0]=true;for(int j=2;j<=n;++j)if(p[j-1]=='*')dp[0][j]=dp[0][j-2];for(int i=1;i<=m;++i)for(int j=1;j<=n;++j)if(p[j-1]=='*')dp[i][j]=dp[i][j-2]||((p[j-2]=='.'||p[j-2]==s[i-1])&&dp[i-1][j]);else dp[i][j]=(p[j-1]=='.'||p[j-1]==s[i-1])&&dp[i-1][j-1];return dp[m][n];}

// 新增：打家劫舍（二）：首尾不能同时取，分别计算 [0,n-2] 与 [1,n-1]。
int robRange(vector<int>&a,int l,int r){int x=0,y=0;for(int i=l;i<=r;++i){int z=max(y,x+a[i]);x=y;y=z;}return y;}
int robCircle(vector<int>&a){if(a.size()==1)return a[0];return max(robRange(a,0,a.size()-2),robRange(a,1,a.size()-1));}

// 新增：股票 II/III：II 累加所有上涨；III 用四个状态表示两次交易的持有/卖出。
int stockUnlimited(vector<int>&p){int ans=0;for(int i=1;i<p.size();++i)ans+=max(0,p[i]-p[i-1]);return ans;}
int stockTwo(vector<int>&p){int buy1=INT_MIN,sell1=0,buy2=INT_MIN,sell2=0;for(int x:p){buy1=max(buy1,-x);sell1=max(sell1,buy1+x);buy2=max(buy2,sell1-x);sell2=max(sell2,buy2+x);}return sell2;}


```

### P2-2 二分与综合变式

- **普通二分**：先定义区间是闭区间还是半开区间，再统一 `l/r` 更新；不要边写边改边界。
- **搜索二维矩阵**：若每行首元素大于前行末元素，可把矩阵视为一维；若只保证行列有序，从右上角向左/下走。
- **排序边界**：找第一个 `>= target` 用 `lower_bound` 思路；找第一个 `> target` 用 `upper_bound` 思路；答案不存在时明确返回位置。
- **答案二分**：把“是否能在答案 `x` 下完成”写成单调 `check(x)`，在可行/不可行边界上二分，而不是二分原数组。
- **验收**：能说清 `check(mid)` 为什么单调；能处理答案在最小值、最大值、无解和重复值的情况。

## 五、每道题的关键注释代码

下面代码默认使用：

```cpp
#include <bits/stdc++.h>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};
```


- **新增题目**：**新增**二分查找-I、**新增**寻找峰值、**新增**数组中的逆序对、**新增**旋转数组的最小数字、**新增**比较版本号。

### 新增题目代码（新增）

```cpp
// 新增：二分查找：区间 [l,r] 闭合，所有分支都排除 mid，避免死循环。
int binarySearch(vector<int>& a, int target) {
    int l = 0, r = (int)a.size() - 1;
    while (l <= r) { int m = l + (r - l) / 2;
        if (a[m] == target) return m; if (a[m] < target) l = m + 1; else r = m - 1; }
    return -1;
}

// 新增：峰值：若 a[mid] < a[mid+1]，峰值必在右侧，否则在左侧含 mid 的区间。
int findPeak(vector<int>& a) {
    int l = 0, r = a.size() - 1;
    while (l < r) { int m = l + (r - l) / 2; if (a[m] < a[m + 1]) l = m + 1; else r = m; }
    return l;
}

// 新增：逆序对：归并时左值大于右值，则左半段剩余元素全部构成逆序对。
long long mergeCount(vector<int>& a, int l, int r, vector<int>& t) {
    if (l >= r) return 0; int m = (l + r) / 2; long long ans = mergeCount(a,l,m,t)+mergeCount(a,m+1,r,t);
    int i=l,j=m+1,k=l; while(i<=m&&j<=r) if(a[i]<=a[j]) t[k++]=a[i++]; else ans+=m-i+1,t[k++]=a[j++];
    while(i<=m)t[k++]=a[i++]; while(j<=r)t[k++]=a[j++]; for(i=l;i<=r;++i)a[i]=t[i]; return ans;
}

// 新增：旋转数组最小值：有重复值时 nums[mid]==nums[r] 只能安全收缩右边界。
int minRotated(vector<int>& a) {
    int l=0,r=a.size()-1; while(l<r){int m=l+(r-l)/2; if(a[m]<a[r])r=m; else if(a[m]>a[r])l=m+1; else --r;} return a[l];
}

// 新增：版本号：逐段解析数字，缺失段按 0 处理，避免直接按字符串比较。
int compareVersion(string a, string b) {
    int i=0,j=0; while(i<a.size()||j<b.size()){ long long x=0,y=0;
        while(i<a.size()&&a[i]!='.') x=x*10+a[i++]-'0'; while(j<b.size()&&b[j]!='.') y=y*10+b[j++]-'0';
        if(x!=y)return x<y?-1:1; ++i; ++j; } return 0;
}


```

### P0-1 数组与哈希

```cpp
// 两数之和：map 的 key 存“还需要的数”，value 存它出现的位置。
vector<int> twoSum(vector<int>& numbers, int target) {
    unordered_map<int, int> need;
    for (int i = 0; i < (int)numbers.size(); ++i) {
        // 如果当前数正好是之前某个数需要的数，答案已找到。
        if (need.count(numbers[i]))
            return {need[numbers[i]] + 1, i + 1}; // 题目下标从 1 开始
        // 先查后存，避免同一个元素被使用两次。
        need[target - numbers[i]] = i;
    }
    return {};
}

// 和为 K 的子数组：prefix[j] - prefix[i] = k。
int subarraySum(vector<int>& nums, int k) {
    unordered_map<int, int> freq;
    freq[0] = 1; // 空前缀，支持从下标 0 开始的答案
    int prefix = 0, ans = 0;
    for (int x : nums) {
        prefix += x;
        // 之前出现过 prefix-k 的每个位置，都能和当前位置组成答案。
        ans += freq[prefix - k];
        ++freq[prefix];
    }
    return ans;
}

// 缺失的第一个正数：把数字 x 放到下标 x-1，最后第一个错位位置就是答案。
int firstMissingPositive(vector<int>& nums) {
    // //记录所有出现的数字
    // unordered_map<int, int> mp;
    // for (int num : nums) {
    //     mp[num]++;
    // }

    // // 不变量 ：对于一个size为n的数组缺失的第一个正整数的数值范围 [1,n+1]
    // //特殊例子 nums = {1,2,3};  最大值的情况：数组元素从1顺序递增，则为n+1 最小值是1
    // //线性遍历 数值范围
    // for (int i = 1; i <= nums.size() + 1; i++) {
    //     if (mp.find(i) == mp.end()) return i;
    // }

    // return 1;
    
    int n = nums.size();
    for (int& x : nums) {
        if (x <= 0 || x > n) x = n + 1; // 这些值不可能是 1..n 的答案
    }
    for (int x : nums) {
        int value = abs(x);
        if (value <= n) nums[value - 1] = -abs(nums[value - 1]); //把在可能范围的值变成负数
    }
    for (int i = 0; i < n; ++i)
        if (nums[i] > 0) return i + 1;
    return n + 1;
}

// 旋转数组：整体反转，再反转前 k 个和后 n-k 个。
void reversePart(vector<int>& nums, int l, int r) {
    while (l < r) swap(nums[l++], nums[r--]);
}
void rotate(vector<int>& nums, int k) {
    int n = nums.size();
    if (n == 0) return;
    k %= n; // k 可能大于 n
    reversePart(nums, 0, n - 1);
    reversePart(nums, 0, k - 1);
    reversePart(nums, k, n - 1);
}

// 除自身以外数组的乘积：先把左侧乘积写入答案，再乘上右侧乘积。
vector<int> productExceptSelf(vector<int>& nums) {
    int n = nums.size();
    vector<int> ans(n, 1);
    int left = 1;
    for (int i = 0; i < n; ++i) {
        ans[i] = left; // 当前下标左边所有数的乘积
        left *= nums[i];
    }
    int right = 1;
    for (int i = n - 1; i >= 0; --i) {
        ans[i] *= right; // 乘上右边所有数的乘积
        right *= nums[i];
    }
    return ans;
}
```

### P0-2 双指针与滑动窗口

```cpp
// 合并有序数组：从尾部写，避免覆盖 nums1 中还未读取的元素。
void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
    int i = m - 1, j = n - 1, write = m + n - 1;
    while (j >= 0) { //A未进行交换的元素保持原位即可
        if (i >= 0 && nums1[i] > nums2[j]) nums1[write--] = nums1[i--]; //比较两数组的尾部，将较大值(当前未合并数据的最大值)复制到尾部下标处
        else nums1[write--] = nums2[j--];
    }
}

// 三数之和：排序后固定 nums[i]，剩余区间用左右指针。
vector<vector<int>> threeSum(vector<int>& nums) {
    // 三元组（a、b、c）中的元素必须按非降序排列。（即a≤b≤c）
    // 解集中不能包含重复的三元组。

    // // 排序后固定 nums[i]，剩余区间用左右指针。
    sort(num.begin(), num.end());
    vector<vector<int>> ans;
    for(int i = 0; i < num.size(); i++){
        if(i > 0 && num[i] == num[i - 1]) continue; // 固定数去重

        int l = i + 1, r = num.size() - 1; //左右指针，和 > 0 则右指针前移，和 < 0 则左指针后移
        while(l < r){
            int sum = num[i] + num[l] + num[r];

            if(sum == 0){
                ans.push_back({num[i], num[l], num[r]});
                while(l < r && num[l] == num[l + 1]) ++l; // 固定数去重
                while(l < r && num[r] == num[r - 1]) --r; // 固定数去重
                ++l;--r;
            } else if(sum < 0) ++l;
            else --r;
        }
    }
    
    return ans;
}

// 盛最多水：木桶效应，面积受较短边限制，移动较长边不会带来更优解。
int maxArea(vector<int>& height) {
    // 盛最多水：木桶效应，面积受较短边限制，移动较长边不会带来更优解。
    int l = 0, r = height.size() - 1, ans = 0;
    while (l < r) {
        ans = max(ans, min(height[l], height[r]) * (r - l));
        if(height[l] < height[r]) l++; //移动较短边才可能得到更大容量
        else r--;
    }

    return ans;
}

// 接雨水：leftMax/rightMax 是当前位置两侧最高柱子。
int trap(vector<int>& height) {
    // 接雨水：leftMax/rightMax 是当前位置两侧最高柱子。
    int l = 0, r = arr.size() - 1, leftMax = 0, rightMax = 0, ans = 0;
    while (l < r) {
        if (arr[l] < arr[r]) { //哪边较低则水量由哪边的最高柱决定，当前位置水量 = 较低边的最高柱值 - 当前位置高度
            leftMax = max(leftMax, arr[l]);
            ans += leftMax - arr[l++]; // 左边较低，所以左侧水量已确定
        } else {
            rightMax = max(rightMax, arr[r]); // 右边较低，所以右侧水量已确定
            ans += rightMax - arr[r--];
        }
    }
    return ans;
}

// 无重复字符最长子串：窗口始终保持无重复。
int lengthOfLongestSubstring(string s) {
    vector<int> last(128, -1); //以字符本身为数组索引记录每个字符出现的最新下标
    int l = 0,ans = 0; //快慢指针。而非左右指针
    for(int r = 0; r < s.size(); r++){
        //在判断 s[right] 之前，[left, right-1] 一定是一个无重复字符的合法窗口，循环不变量
        l = max(l, last[s[r]] + 1); // 左端点不能回退
        last[s[r]] = r; //当前字符出现的最新位置就是 right
        ans = max(ans, r - l + 1); //取较大值：已遍历窗口的最大长度，当前无重复字符窗口的长度
    }
    return ans;
}

// 字母异位词：固定长度窗口维护 26 个字符的差值。
vector<int> findAnagrams(string s, string p) {
    // 字母异位词：固定长度窗口维护 26 个字符的差值。
    vector<int> need(26), window(26), ans;
    for(char c : p) ++need[c - 'a'];
    for(int i = 0; i < s.size(); ++i){
        ++window[s[i] - 'a'];
        if(i >= p.size()) --window[s[i -p.size()] - 'a'];//控制窗口长度和 p 相同
        if(need == window) ans.push_back(i - p.size() + 1);//保存当前窗口起始索引
    } 
    return ans;
}
```

### P0-3 链表

```cpp
// 反转链表：先保存 next，再改变当前节点指向，避免断链。
ListNode* reverseList(ListNode* head) {
    // 反转链表：先保存 next，再改变当前节点指向，避免断链。

    ListNode* prev = nullptr;
    while(head){
        ListNode* next = head->next; //包括后面的节点都是先保存再改变指向
        head->next = prev;
        prev = head;
        head = next;
    }
    return prev;
}

// 相交链表（第一个公共结点）：两个指针分别走 A+B、B+A，最终到达同一个地址或 nullptr。
ListNode* FindFirstCommonNode( ListNode* pHead1, ListNode* pHead2) {
    // 相交链表（第一个公共结点）：两个指针分别走 A+B、B+A，最终到达同一个地址或 nullptr。
    ListNode *p1 = pHead1, *p2 = pHead2;
    while(p1 != p2){ //最终到达同一个地址或 nullptr(无相交)。
        p1 = p1 ? p1->next : pHead2;
        p2 = p2 ? p2->next : pHead1;
    }
    return p1;
}

// 环入口：相遇后，一个指针回到头部，两者每次走一步再次相遇即入口。
ListNode* EntryNodeOfLoop(ListNode* pHead) {
    // 环入口：相遇后，一个指针回到头部，两者每次走一步再次相遇即入口。 L 为环前链长，C 为环长度，x为 fast 离环入口的距离, L = KC - x = (K - 1)C + (C -x)，因此 slow 从头走完 L，fast 正好走完(K - 1)C + (C -x)
    ListNode *slow = pHead, *fast = pHead;
    do {
        if(!fast || !fast->next) return nullptr;
        slow = slow->next; fast = fast->next->next;
    } while(slow != fast); //相遇则止
    slow = pHead; //slow 从头开始走
    while(slow != fast) {slow = slow->next; fast = fast->next; }
    return slow;
}

// 回文链表：找到后半段并反转，逐个比较前后两半。
ListNode* reverseList(ListNode* head){
        ListNode* prev = nullptr;
        while(head){
            ListNode* next = head->next;
            head->next = prev;
            prev = head;
            head = next;
        }

        return prev;
}

bool isPalindrome(ListNode* head) {
    // 回文链表：找到后半段并反转，逐个比较前后两半。
    ListNode* slow = head, *fast = head;
    while(fast && fast->next){
        slow = slow->next;
        fast = fast->next->next;
    }

    ListNode* right = reverseList(slow); //slow 可视为链表后半段的头节点
    //为什么用 right 非空作为判断条件，而不用 left，因为前半段最后一个节点的 next 并没有改变指向
    for(ListNode* left = head; right; left = left->next, right = right->next){
        if(left->val != right->val) return false;
    }
    return true;
}

// K 个一组翻转：先找到本组尾部，节点不足 K 个就保持原样。
ListNode* reverseKGroup(ListNode* head, int k) {
    // K 个一组翻转：先找到本组尾部，节点不足 K 个就保持原样。
    ListNode dummy(0);
    dummy.next = head;
    ListNode* groupPrev = &dummy;//groupPrev 即待翻转组的前一节点，groupPrev 的 next 指向待翻转组的头节点

    while(true){
        ListNode* kth = groupPrev;
        for(int i = 0; i < k && kth; ++i) kth = kth->next; //找到待翻转组的尾部
        if(!kth) break;

        ListNode* groupNext = kth->next;// groupNext 即下一组待翻转的头节点
        //以下是链表的每组反转逻辑
        ListNode* prev = groupNext, *cur = groupPrev->next;
        while(cur != groupNext){
            ListNode* next = cur->next;
            cur->next = prev;
            prev = cur;
            cur = next;
        }

        ListNode* oldHead = groupPrev->next;//旧头节点即翻转后那一组的尾节点，即下一组的前一个节点
        groupPrev->next = kth;//groupPrev 的 next 指向待翻转组的头节点
        groupPrev = oldHead;//groupPrev 即待翻转组的前一节点
    }

    return dummy.next;
}

// LRU：链表头是最近使用，尾是最久未使用；unordered_map O(1) 找节点。
class Solution {
    int cap;
    list<pair<int, int>> order; // front: 最近使用
    unordered_map<int, list<pair<int, int>>::iterator> pos;
  public:
    Solution(int capacity) : cap(capacity){
        // write code here
        if(cap < 0) throw("error: capacity < 0");
        pos.reserve(cap);
    }
    // LRU：链表头是最近使用，尾是最久未使用；unordered_map O(1) 找节点。
    // 先实现 set，再实现 get
    // set: 若存在则先删除，将节点添加到链表头，若添加后 size > cap 则移除链表最后一个元素
    // get: 若找到则先保存值后删除节点，再重新添加到链表头部

    int get(int key){
        if (!pos.count(key)) return -1;
        // 找到则先删除后添加到链表头部
        auto it = pos[key]; 
        int value = it->second;
        order.erase(it);
        order.push_front({key, value});
        pos[key] = order.begin();
        return value;
    }

    void set(int key, int value){
        if(pos.count(key)) order.erase(pos[key]);
        order.push_front({key, value});
        pos[key] = order.begin();
        if(order.size() > cap){
            //移除链表最后一个元素，即最久未使用的元素
            int oldKey = order.back().first;
            pos.erase(oldKey); //按照 Key 删除
            order.pop_back(); //移除最久未使用的元素
        }
    }
};
```

### P0-4 栈与单调栈

```cpp
// 最小栈：minStack[i] 表示到当前层为止的最小值。
class MinStack {
    // 最小栈：双栈法，minStack[i] 表示到当前层为止的最小值。
    stack<int> st, minSt;
public:
    void push(int value) {
        st.push(value);
        // minSt 压入当前 st 所有原始元素的最小值
        minSt.push(minSt.empty() ? value : std::min(value, minSt.top()));
    }
    void pop() { 
        st.pop();
        minSt.pop();
     }
    int top() { 
        return st.top();
     }
    int min() { 
        return minSt.top();
     }
};

// 字符串解码：遇到 '[' 保存外层状态，遇到 ']' 恢复并拼接当前层。
string decodeString(string s) {
    // 字符串解码：遇到 '[' 保存外层状态，遇到 ']' 恢复并拼接当前层。
    stack<int> counts;
    stack<string> texts;
    int num = 0;
    string cur;
    for(char c : s){
        //遇到 数字字符 转换成 数值
        if(c >= '0' && c <= '9') num = num * 10 + c - '0'; 
        else if(c == '['){
            //遇到 '[' 保存外层状态
            counts.push(num);
            texts.push(cur);
            num = 0;
            cur.clear();
        }else if(c == ']'){
            //遇到 ']' 恢复并拼接当前层
            string prev = texts.top();
            texts.pop();
            int times = counts.top();
            counts.pop();
            while(times--) prev += cur;
            cur = prev;
        } else cur += c; //遇到 字母字符 进行拼接
    }
    return cur;
}

// 每日温度：递减栈保存还没找到更高温度的下标。
vector<int> dailyTemperatures(vector<int>& t) {
    vector<int> ans(t.size()); stack<int> st;
    for (int i = 0; i < (int)t.size(); ++i) {
        while (!st.empty() && t[i] > t[st.top()]) {
            int j = st.top(); st.pop();
            ans[j] = i - j; // i 是 j 右侧第一个更高温度
        }
        st.push(i);
    }
    return ans; // 栈中剩余下标没有更高温度，默认 0
}

// 柱状图最大矩形：递增栈，出栈时确定右边界；首尾哨兵统一处理剩余柱子。
int largestRectangleArea(vector<int> heights) {
    heights.insert(heights.begin(), 0);
    heights.push_back(0);
    stack<int> st; st.push(0);
    int ans = 0;
    for (int i = 1; i < (int)heights.size(); ++i) {
        while (heights[i] < heights[st.top()]) {
            int h = heights[st.top()]; st.pop();
            int width = i - st.top() - 1; // 新栈顶右侧到 i 左侧
            ans = max(ans, h * width);
        }
        st.push(i);
    }
    return ans;
}
```

### P0-5 二叉树基础

```cpp
// DFS：先序位置处理当前节点；把处理逻辑放在不同位置即可得到中序/后序。
void dfs(TreeNode* root) {
    if (!root) return;
    // 这里是前序位置
    dfs(root->left);
    // 这里是中序位置
    dfs(root->right);
    // 这里是后序位置
}

// BFS：每轮固定 size，保证这一轮只处理一层。
vector<vector<int>> levelOrder(TreeNode* root) {
    vector<vector<int>> ans; if (!root) return ans;
    queue<TreeNode*> q; q.push(root);
    while (!q.empty()) {
        int size = q.size(); vector<int> level;
        while (size--) {
            TreeNode* node = q.front(); q.pop(); level.push_back(node->val);
            if (node->left) q.push(node->left);
            if (node->right) q.push(node->right);
        }
        ans.push_back(level);
    }
    return ans;
}

// BST 第 K 小：BST 的中序遍历天然是升序。
int kthSmallest(TreeNode* root, int k) {
    stack<TreeNode*> st;
    while (true) {
        while (root) { st.push(root); root = root->left; }
        root = st.top(); st.pop();
        if (--k == 0) return root->val;
        root = root->right;
    }
}

// 路径和 III：前缀和 cur-target 的出现次数，就是以当前节点结尾的合法路径数。
int pathDfs(TreeNode* node, long long cur, long long target,
            unordered_map<long long, int>& freq) {
    if (!node) return 0;
    cur += node->val;
    int ans = freq[cur - target];
    ++freq[cur];
    ans += pathDfs(node->left, cur, target, freq);
    ans += pathDfs(node->right, cur, target, freq);
    --freq[cur]; // 离开当前分支，不能污染兄弟分支
    return ans;
}
int pathSum(TreeNode* root, int targetSum) {
    unordered_map<long long, int> freq{{0, 1}};
    return pathDfs(root, 0, targetSum, freq);
}

// 前序 + 中序构造：前序当前段第一个是根，中序中的根切分左右子树。
TreeNode* build(vector<int>& pre, int pl, int pr, vector<int>& in, int il, int ir,
                unordered_map<int, int>& where) {
    if (pl > pr) return nullptr;
    TreeNode* root = new TreeNode(pre[pl]);
    int mid = where[root->val], leftSize = mid - il;
    root->left = build(pre, pl + 1, pl + leftSize, in, il, mid - 1, where);
    root->right = build(pre, pl + leftSize + 1, pr, in, mid + 1, ir, where);
    return root;
}
TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
    unordered_map<int, int> where;
    for (int i = 0; i < (int)inorder.size(); ++i) where[inorder[i]] = i;
    return build(preorder, 0, preorder.size() - 1, inorder, 0, inorder.size() - 1, where);
}

// 右视图：每层最后弹出的节点就是从右侧看到的节点。
vector<int> rightSideView(TreeNode* root) {
    vector<int> ans; if (!root) return ans;
    queue<TreeNode*> q; q.push(root);
    while (!q.empty()) {
        int size = q.size();
        while (size--) {
            TreeNode* node = q.front(); q.pop();
            if (size == 0) ans.push_back(node->val);
            if (node->left) q.push(node->left);
            if (node->right) q.push(node->right);
        }
    }
    return ans;
}
```

### P0-6 动态规划基础

```cpp
// 打家劫舍：prev2/prev1 分别表示前两个位置的最优答案。
int rob(vector<int>& nums) {
    int prev2 = 0, prev1 = 0;
    for (int money : nums) {
        int take = prev2 + money;
        int skip = prev1;
        prev2 = prev1; prev1 = max(take, skip);
    }
    return prev1;
}

// 零钱兑换：dp[x] 是凑出金额 x 的最少硬币数；不可达用 INF 表示。
int coinChange(vector<int>& coins, int amount) {
    const int INF = amount + 1;
    vector<int> dp(amount + 1, INF); dp[0] = 0;
    for (int x = 1; x <= amount; ++x)
        for (int coin : coins)
            if (coin <= x) dp[x] = min(dp[x], dp[x - coin] + 1);
    return dp[amount] == INF ? -1 : dp[amount];
}

// 完全平方数：最后一个平方数为 j*j，枚举前一个状态。
int numSquares(int n) {
    vector<int> dp(n + 1, n + 1); dp[0] = 0;
    for (int i = 1; i <= n; ++i)
        for (int j = 1; j * j <= i; ++j)
            dp[i] = min(dp[i], dp[i - j * j] + 1);
    return dp[n];
}

// LIS 的 O(n^2) 版本：dp[i] 表示以 nums[i] 结尾的最长递增长度。
int lengthOfLIS(vector<int>& nums) {
    vector<int> dp(nums.size(), 1); int ans = 0;
    for (int i = 0; i < (int)nums.size(); ++i) {
        for (int j = 0; j < i; ++j)
            if (nums[j] < nums[i]) dp[i] = max(dp[i], dp[j] + 1);
        ans = max(ans, dp[i]);
    }
    return ans;
}

// 最小路径和：当前位置只能从上方或左方到达。
int minPathSum(vector<vector<int>>& grid) {
    int m = grid.size(), n = grid[0].size();
    vector<int> dp(n, INT_MAX); dp[0] = 0;
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            if (j > 0) dp[j] = min(dp[j], dp[j - 1]);
            dp[j] += grid[i][j];
        }
    }
    return dp[n - 1];
}

// LCS：相等时从左上角转移，否则取上方/左方较大值。
int longestCommonSubsequence(string a, string b) {
    int m = a.size(), n = b.size();
    vector<vector<int>> dp(m + 1, vector<int>(n + 1));
    for (int i = 1; i <= m; ++i)
        for (int j = 1; j <= n; ++j)
            dp[i][j] = a[i - 1] == b[j - 1]
                ? dp[i - 1][j - 1] + 1
                : max(dp[i - 1][j], dp[i][j - 1]);
    return dp[m][n];
}
```

### P1-1 排序与堆

```cpp
// 冒泡排序：每轮把未排序区间的最大值交换到末尾；本轮无交换即可提前结束。
void bubbleSort(vector<int>& a) {
    for (int end = (int)a.size() - 1; end > 0; --end) {
        bool swapped = false;
        for (int i = 0; i < end; ++i) {
            if (a[i] > a[i + 1]) {
                swap(a[i], a[i + 1]);
                swapped = true;
            }
        }
        if (!swapped) break;
    }
}

// 快排：partition 返回 pivot 最终位置，递归区间必须严格缩小。
int partition(vector<int>& a, int l, int r) {
    int pivot = a[r], i = l;
    for (int j = l; j < r; ++j)
        if (a[j] <= pivot) swap(a[i++], a[j]);
    swap(a[i], a[r]); return i;
}
void quickSort(vector<int>& a, int l, int r) {
    if (l >= r) return;
    int p = partition(a, l, r);
    quickSort(a, l, p - 1); quickSort(a, p + 1, r);
}

// 归并：两个子区间已经有序，每次取当前较小值。
void mergeSort(vector<int>& a, int l, int r, vector<int>& temp) {
    if (l >= r) return;
    int mid = l + (r - l) / 2;
    mergeSort(a, l, mid, temp); mergeSort(a, mid + 1, r, temp);
    int i = l, j = mid + 1, k = l;
    while (i <= mid && j <= r) temp[k++] = a[i] <= a[j] ? a[i++] : a[j++];
    while (i <= mid) temp[k++] = a[i++];
    while (j <= r) temp[k++] = a[j++];
    for (i = l; i <= r; ++i) a[i] = temp[i];
}

// 堆排序：先建大顶堆，再把堆顶最大值放到数组末尾。
void heapify(vector<int>& a, int n, int i) {
    int largest = i, l = 2 * i + 1, r = 2 * i + 2;
    if (l < n && a[l] > a[largest]) largest = l;
    if (r < n && a[r] > a[largest]) largest = r;
    if (largest != i) { swap(a[i], a[largest]); heapify(a, n, largest); }
}
void heapSort(vector<int>& a) {
    for (int i = a.size() / 2 - 1; i >= 0; --i) heapify(a, a.size(), i);
    for (int end = a.size() - 1; end > 0; --end) {
        swap(a[0], a[end]); heapify(a, end, 0);
    }
}

// Top K：小顶堆只保留当前最大的 K 个元素，堆顶是第 K 大候选。
int kthLargest(vector<int>& nums, int k) {
    priority_queue<int, vector<int>, greater<int>> pq;
    for (int x : nums) {
        pq.push(x);
        if ((int)pq.size() > k) pq.pop();
    }
    return pq.top();
}

// 数据流中位数：左边用大顶堆，右边用小顶堆，保持左边不少于右边且最多多一个。
class MedianFinder {
    priority_queue<int> left;
    priority_queue<int, vector<int>, greater<int>> right;
public:
    void addNum(int num) {
        if (left.empty() || num <= left.top()) left.push(num);
        else right.push(num);
        if (left.size() < right.size()) { left.push(right.top()); right.pop(); }
        if (left.size() > right.size() + 1) { right.push(left.top()); left.pop(); }
    }
    double findMedian() {
        if (left.size() > right.size()) return left.top();
        return (left.top() + right.top()) / 2.0;
    }
};
```

### P1-2 回溯与矩阵

```cpp
// 括号生成：右括号数量不能超过左括号，否则前缀已经非法。
void gen(string cur, int left, int right, int n, vector<string>& ans) {
    if ((int)cur.size() == 2 * n) { ans.push_back(cur); return; }
    if (left < n) gen(cur + '(', left + 1, right, n, ans);
    if (right < left) gen(cur + ')', left, right + 1, n, ans);
}
vector<string> generateParenthesis(int n) {
    vector<string> ans; gen("", 0, 0, n, ans); return ans;
}

// 单词搜索：进入格子时标记为已访问，返回时恢复，保证不同路径互不影响。
bool wordDfs(vector<vector<char>>& board, string& word, int i, int j, int k) {
    if (k == (int)word.size()) return true;
    if (i < 0 || i >= board.size() || j < 0 || j >= board[0].size() ||
        board[i][j] != word[k]) return false;
    char saved = board[i][j]; board[i][j] = '#';
    bool ok = wordDfs(board, word, i + 1, j, k + 1) ||
              wordDfs(board, word, i - 1, j, k + 1) ||
              wordDfs(board, word, i, j + 1, k + 1) ||
              wordDfs(board, word, i, j - 1, k + 1);
    board[i][j] = saved;
    return ok;
}
bool exist(vector<vector<char>>& board, string word) {
    for (int i = 0; i < board.size(); ++i)
        for (int j = 0; j < board[0].size(); ++j)
            if (wordDfs(board, word, i, j, 0)) return true;
    return false;
}

// 矩阵置零：第一行/列充当标记位，先保存它们原本是否含 0。
void setZeroes(vector<vector<int>>& matrix) {
    int m = matrix.size(), n = matrix[0].size();
    bool firstRow = false, firstCol = false;
    for (int j = 0; j < n; ++j) firstRow |= matrix[0][j] == 0;
    for (int i = 0; i < m; ++i) firstCol |= matrix[i][0] == 0;
    for (int i = 1; i < m; ++i)
        for (int j = 1; j < n; ++j)
            if (matrix[i][j] == 0) matrix[i][0] = matrix[0][j] = 0;
    for (int i = 1; i < m; ++i)
        for (int j = 1; j < n; ++j)
            if (matrix[i][0] == 0 || matrix[0][j] == 0) matrix[i][j] = 0;
    if (firstRow) fill(matrix[0].begin(), matrix[0].end(), 0);
    if (firstCol) for (auto& row : matrix) row[0] = 0;
}

// 螺旋矩阵：每走一条边就收缩对应边界，并检查是否已经越界。
vector<int> spiralOrder(vector<vector<int>>& matrix) {
    vector<int> ans; int top = 0, bottom = matrix.size() - 1;
    int left = 0, right = matrix[0].size() - 1;
    while (top <= bottom && left <= right) {
        for (int j = left; j <= right; ++j) ans.push_back(matrix[top][j]); ++top;
        for (int i = top; i <= bottom; ++i) ans.push_back(matrix[i][right]); --right;
        if (top <= bottom) { for (int j = right; j >= left; --j) ans.push_back(matrix[bottom][j]); --bottom; }
        if (left <= right) { for (int i = bottom; i >= top; --i) ans.push_back(matrix[i][left]); ++left; }
    }
    return ans;
}

// 旋转图像：转置后每一行反转，等价于顺时针旋转 90 度。
void rotateImage(vector<vector<int>>& matrix) {
    int n = matrix.size();
    for (int i = 0; i < n; ++i)
        for (int j = i + 1; j < n; ++j) swap(matrix[i][j], matrix[j][i]);
    for (auto& row : matrix) reverse(row.begin(), row.end());
}
```

### P1-3 贪心与技巧

```cpp
// 买卖股票：当天卖出时，最佳买入点只可能是此前最低价。
int maxProfit(vector<int>& prices) {
    int minPrice = INT_MAX, ans = 0;
    for (int price : prices) { minPrice = min(minPrice, price); ans = max(ans, price - minPrice); }
    return ans;
}

// 异或：相同数字互相抵消，最后只剩只出现一次的数字。
int singleNumber(vector<int>& nums) {
    int ans = 0;
    for (int x : nums) ans ^= x;
    return ans;
}

// 摩尔投票：candidate 与不同数字抵消；题目若不保证多数存在，需要再次计数验证。
int majorityElement(vector<int>& nums) {
    int candidate = 0, count = 0;
    for (int x : nums) {
        if (count == 0) candidate = x;
        count += (x == candidate ? 1 : -1);
    }
    return candidate;
}

// 颜色分类：维护 [0, zero)、[zero, cur) 是 0/1，[cur, two] 未处理，[two+1,n) 是 2。
void sortColors(vector<int>& nums) {
    int zero = 0, cur = 0, two = nums.size() - 1;
    while (cur <= two) {
        if (nums[cur] == 0) swap(nums[zero++], nums[cur++]);
        else if (nums[cur] == 2) swap(nums[cur], nums[two--]); // cur 位置换来的数尚未检查
        else ++cur;
    }
}

// 下一个排列：找到最长非增后缀，交换拐点与右侧第一个更大的数，再反转后缀。
void nextPermutation(vector<int>& nums) {
    int i = nums.size() - 2;
    while (i >= 0 && nums[i] >= nums[i + 1]) --i;
    if (i >= 0) {
        int j = nums.size() - 1;
        while (nums[j] <= nums[i]) --j;
        swap(nums[i], nums[j]);
    }
    reverse(nums.begin() + i + 1, nums.end()); // i=-1 时反转整个数组
}
```

### P2-1 DP 进阶

```cpp
// 乘积最大子数组：负数会让最大值和最小值互换，因此两者都要保存。
int maxProduct(vector<int>& nums) {
    int hi = nums[0], lo = nums[0], ans = nums[0];
    for (int i = 1; i < (int)nums.size(); ++i) {
        int x = nums[i], oldHi = hi, oldLo = lo;
        hi = max({x, oldHi * x, oldLo * x});
        lo = min({x, oldHi * x, oldLo * x});
        ans = max(ans, hi);
    }
    return ans;
}

// 最长回文子串：区间长度从短到长，dp[l][r] 依赖更短区间。
string longestPalindrome(string s) {
    int n = s.size(), bestL = 0, bestLen = 1;
    vector<vector<bool>> dp(n, vector<bool>(n));
    for (int len = 1; len <= n; ++len)
        for (int l = 0; l + len <= n; ++l) {
            int r = l + len - 1;
            dp[l][r] = s[l] == s[r] && (len <= 2 || dp[l + 1][r - 1]);
            if (dp[l][r] && len > bestLen) bestL = l, bestLen = len;
        }
    return s.substr(bestL, bestLen);
}

// 编辑距离：最后一步是插入、删除或替换，取三者最小值。
int minDistance(string a, string b) {
    int m = a.size(), n = b.size(); vector<vector<int>> dp(m + 1, vector<int>(n + 1));
    for (int i = 0; i <= m; ++i) dp[i][0] = i;
    for (int j = 0; j <= n; ++j) dp[0][j] = j;
    for (int i = 1; i <= m; ++i) for (int j = 1; j <= n; ++j)
        dp[i][j] = a[i - 1] == b[j - 1] ? dp[i - 1][j - 1]
            : 1 + min({dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]});
    return dp[m][n];
}

// 最长有效括号：栈放下标，栈底是当前合法段之前的边界。
int longestValidParentheses(string s) {
    stack<int> st; st.push(-1); int ans = 0;
    for (int i = 0; i < (int)s.size(); ++i) {
        if (s[i] == '(') st.push(i);
        else {
            st.pop();
            if (st.empty()) st.push(i); // i 成为新的非法边界
            else ans = max(ans, i - st.top());
        }
    }
    return ans;
}

// 单词拆分：dp[i] 表示 s[0..i) 能否被字典拆出，枚举最后一个单词。
bool wordBreak(string s, vector<string>& wordDict) {
    unordered_set<string> dict(wordDict.begin(), wordDict.end());
    vector<bool> dp(s.size() + 1); dp[0] = true;
    for (int i = 1; i <= (int)s.size(); ++i)
        for (int j = 0; j < i; ++j)
            if (dp[j] && dict.count(s.substr(j, i - j))) { dp[i] = true; break; }
    return dp[s.size()];
}
```

### P2-2 二分与综合变式

```cpp
// 搜索二维矩阵：每行首元素大于上一行末元素时，可视为一维有序数组。
bool searchMatrix(vector<vector<int>>& matrix, int target) {
    int m = matrix.size(), n = matrix[0].size(), l = 0, r = m * n - 1;
    while (l <= r) {
        int mid = l + (r - l) / 2, value = matrix[mid / n][mid % n];
        if (value == target) return true;
        if (value < target) l = mid + 1; else r = mid - 1;
    }
    return false;
}

// 排序边界：lower_bound 返回第一个 >= target 的位置，区间始终是 [l, r)。
int lowerBound(vector<int>& nums, int target) {
    int l = 0, r = nums.size();
    while (l < r) {
        int mid = l + (r - l) / 2;
        if (nums[mid] < target) l = mid + 1;
        else r = mid;
    }
    return l; // 可能等于 nums.size()，调用方需判断是否越界
}

// 答案二分示例：最小运载能力；capacity 越大，check 越容易成功，具有单调性。
bool canShip(vector<int>& weights, int days, int capacity) {
    int usedDays = 1, load = 0;
    for (int w : weights) {
        if (load + w > capacity) { ++usedDays; load = 0; }
        load += w;
    }
    return usedDays <= days;
}
int shipWithinDays(vector<int>& weights, int days) {
    int l = *max_element(weights.begin(), weights.end());
    int r = accumulate(weights.begin(), weights.end(), 0);
    while (l < r) {
        int mid = l + (r - l) / 2;
        if (canShip(weights, days, mid)) r = mid;
        else l = mid + 1;
    }
    return l;
}
```

## 六、10 天执行计划

| 天数 | 重点 | 必刷任务 | 当天验收 |
|---|---|---|---|
| Day 1 | 数组与哈希 | 两数之和、和为 K、旋转数组 | 能区分频次、首次位置、原地标记 |
| Day 2 | 数组与双指针 | 缺失正数、乘积、合并数组、三数之和 | O(n) 原地题各写一遍，三数之和完成去重 |
| Day 3 | 双指针与窗口 | 盛最多水、接雨水、无重复字符、字母异位词 | 口述窗口不变量和左右指针移动依据 |
| Day 4 | 链表 | 反转、相交、环入口、回文、K 组翻转、LRU | 限时完成 3 题，指针不丢链 |
| Day 5 | 栈与单调栈 | 最小栈、字符串解码、每日温度、柱状图 | 解释栈存值/下标及左右边界 |
| Day 6 | 树与回溯 | DFS/BFS、第 K 小、路径和、构造树、右视图、括号生成 | 写出递归四问和 BFS 分层 |
| Day 7 | DP 基础 | 打家劫舍、零钱兑换、完全平方数、LIS、最小路径和、LCS | 每题先写五句话，再编码 |
| Day 8 | 排序与堆 | 快排、归并、堆、Top K、中位数 | 能选堆而不是无意义完整排序 |
| Day 9 | 回溯、矩阵、贪心 | 单词搜索、矩阵三题、股票、异或、摩尔、颜色分类、下一个排列 | 原地题保护信息，贪心能讲证明 |
| Day 10 | P2 与模拟 | 进阶 DP、搜索矩阵、排序边界、答案二分；随机抽 4 题 | 90 分钟完成至少 3 题并完整复盘 |

> 时间紧时：先完成 Day 1～7 的 P0；不要为了追求题量跳过错题复写。每天建议 2～3 小时：理解 30 分钟、限时手撕 90 分钟、复盘 30 分钟。

## 七、进度与复盘记录

完成度使用：`0` 未开始，`1` 看过但不能写，`2` 能写但不稳定，`3` 限时独立完成并能解释，`4` 随机变式也稳定。

### 1. 每日执行表

| 日期/Day | 今日主题 | 具体任务 | 完成度 | 当前 P0 重点 | 卡点/错误 | 复盘结论 | 下一步 |
|---|---|---|---:|---|---|---|---|
|  |  |  | 0 |  |  |  |  |

### 2. 单题记录表

| 题目 | 模型 | 用时 | 独立完成 | 看提示 | 核心不变量/状态 | 错误原因 | D+1/D+3/D+7 |
|---|---|---:|---|---|---|---|---|
|  |  |  |  |  |  |  |  |

### 3. 周期复盘表

| 周期 | 已完成主题 | P0 掌握率 | 最弱题型 | 重复错误 | 下周期重点 | 调整计划 |
|---|---|---:|---|---|---|---|
| 首轮 |  |  |  |  |  |  |
| 二轮 |  |  |  |  |  |  |

### 错题模板

```text
题目：
所属模型：
第一次错误：边界 / 状态定义 / 指针更新 / 去重 / 初始化 / 复杂度 / C++ 语法
正确不变量或状态：
最小修复：
下次看到什么信号要想到它：
复写日期：D+1 / D+3 / D+7
```

## 八、面试前速记与通过标准

- 哈希：查补数、计频次、记前缀和；需要多个答案时不能覆盖历史频次。
- 双指针/窗口：先找单调性；窗口要说清“表示什么、何时扩张、何时收缩”。
- 链表：虚拟头、保存后继、比较地址、快慢指针、恢复结构。
- 单调栈：存下标；出栈确定右边界，新栈顶确定左边界。
- 树：先定义递归返回值；BFS 按层；BST 中序有序；路径和允许负数时不能错误剪枝。
- DP：状态、转移、初始化、顺序、空间优化，五项缺一不可。
- 堆：默认大顶堆；Top K 通常用大小 K 的小顶堆。
- 回溯：路径、选择、结束、剪枝、撤销。
- 二分：先写单调 `check` 和区间含义，再写边界。
- C++：`long long` 防溢出；检查 `empty()`、下标、`nullptr` 和迭代器失效。

通过标准：P0 连续两次 20 分钟内独立写出且边界通过；P1 25 分钟内写出并能讲替代解；P2 能脱稿讲清状态/不变量、复杂度和边界。任何题都不能只记代码，必须能解释为什么这样移动、转移、出栈、剪枝或选择。
