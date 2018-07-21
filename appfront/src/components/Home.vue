<template>

<div>
  <el-container style="height: 500px; border: 1px solid #eee">
    <el-header style="height: 50px; font-weight: bold">知识图谱标注系统</el-header>
    <el-container>
    
      <el-aside width="200px" >
        <el-menu
          default-active="1"
          class="el-menu-vertical-demo"
          >
          <el-menu-item index="1" v-on:click="setShowTable('TechTable')">
            <i class="el-icon-setting"></i>
            <span slot="title">技术关键词标引</span>
          </el-menu-item>

          <el-menu-item index="2" @click="setShowTable('CompanyTable')">
            <i class="el-icon-menu"></i>
            <span slot="title">企业实体标引</span>
          </el-menu-item>

          <el-menu-item index="3" @click="setShowTable('RelationTable')">
            <i class="el-icon-document"></i>
            <span slot="title">关系标引</span>
          </el-menu-item>
        </el-menu>
      </el-aside>

      <el-main>

    
        


        <template v-if="showTable === 'TechTable'">
          <el-table :data="tableData" key="TechTable">
            <el-table-column prop="keyword" label="关键词" width="140">
              <template slot-scope="scope">
                <span>{{ scope.row.name }}</span>
              </template>
            </el-table-column>
            <el-table-column prop="origin" label="来源" width="280">
              <template slot-scope="scope">

                       <!-- 弹出框 -->
                <el-popover placement="right-start" width="600" trigger="click">
                  <center>
                    <i class="el-icon-share success"></i>
                    <span type="success">{{scope.row.name}}-来源- {{scope.row.news_nums}} 条新闻</span>
                  </center>
                      <el-table :data="newsData" :highlight-current-row="true"   max-height="250">
                          <el-table-column width="150" property="id" label="编号" fixed align="center"></el-table-column>
                          <el-table-column width="150" property="title" label="标题" fixed align="center"></el-table-column>
                          <el-table-column width="150" property="source" label="来源" align="center"></el-table-column>
                          <el-table-column width="150" label="操作" align="center">
                                      <template slot-scope="scope">
                      
                                  <el-button
                                    size="mini"
                                    type="primary"
                                   ><a target="_blank" rel="noopener noreferrer" :href="scope.row.link" style="color:#fff;text-decoration:none">查看</a></el-button>
                                </template>
                          </el-table-column>

          
              </el-table>
                <span slot="reference" @click="newsList('Tech', scope.row.name)">新闻<el-tag type='danger' size="medium" style="margin: 0 5px">{{scope.row.news_nums}}</el-tag></span>
              </el-popover>

                 <!-- 弹出框 -->
                <el-popover placement="right-start" width="600" trigger="click">
                  <center>
                    <i class="el-icon-share success"></i>
                    <span type="success">{{scope.row.name}}-来源- {{scope.row.patent_nums}} 条专利</span>
                  </center>
                      <el-table :data="patentData" :highlight-current-row="true"   max-height="250">
                          <el-table-column width="150" property="id" label="编号" fixed align="center"></el-table-column>
                          <el-table-column width="150" property="title" label="标题" fixed align="center"></el-table-column>
                          <el-table-column width="150" property="source" label="来源" align="center"></el-table-column>
                          <el-table-column width="150" label="操作" align="center">
                                      <template slot-scope="scope">
                      
                                  <el-button
                                    size="mini"
                                    type="primary"
                                   ><a target="_blank" rel="noopener noreferrer" :href="scope.row.link" style="color:#fff;text-decoration:none">查看</a></el-button>
                                </template>
                          </el-table-column>
              </el-table>
                <span slot="reference" @click="patentList(scope.row.name)">专利<el-tag type='danger' size="medium" style="margin: 0 5px">{{scope.row.patent_nums}}</el-tag></span>
              </el-popover>
              </template>
            </el-table-column>
            <el-table-column prop="operation" label="标注">
              <template slot-scope="scope">
                <el-button type="info" size="mini" @click="open">丢弃</el-button>

    <!-- 弹出框 -->
                <el-popover placement="bottom" width="400" trigger="click">

                  <center>
                    <i class="el-icon-share success"></i>
                    <span type="success">同义词</span>
                  </center>
                  <el-table :data="synonymData" :highlight-current-row="true">
                    <el-table-column width="150" property="name" label="同义词"></el-table-column>
                    <el-table-column label="操作">
                      <template slot-scope="scope">
                                <el-button
                                  size="mini"
                                  @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
                                <el-button
                                  size="mini"
                                  type="danger"
                                  @click="handleDelete(scope.$index, scope.row)">删除</el-button>
                              </template>
                    </el-table-column>
                  </el-table>
                
                <el-button type="warning" size="mini" slot="reference" @click="getTechSyn(scope.row.name)">同义词</el-button>
        </el-popover>
                  
                  
 <!-- 弹出框 -->
                <el-popover placement="bottom" width="400" trigger="click">

                  <center>
                    <el-button type="success" size="mini"><i class="el-icon-circle-plus"></i><span type="success">{{scope.row.name}}-新标签</span></el-button>
                  </center>
                  <div class="demo-input-suffix">
                    一级类目
                  <el-input v-model="input_company" placeholder="一级" type="textarea" autosize></el-input>
                  </div>
                  
                  <div class="demo-input-suffix">
                    技术同义词
                  <el-input v-model="input_company_syn" type="textarea" placeholder="同义词 每行一条"></el-input>
                      <center>
                    <div id="add_company_syn">
                      <el-button type="success" @click="addTech()">添加</el-button>
                    </div>
                    </center>
                    </div>
                <el-button type="success" size="mini" slot="reference">新技术标签</el-button>
                </el-popover>
              </template>
            </el-table-column>
          </el-table>
        </template>

        <template v-else-if="showTable === 'CompanyTable'">
          <el-table  :data="tableData" key="CompanyTable">
            <el-table-column prop="name" label="关键词" width="140">
              <template slot-scope="scope">
                <span>{{ scope.row.name }}</span>
              </template>
            </el-table-column>
            <el-table-column prop="origin" label="来源" width="280">
              <template slot-scope="scope">
                <!-- 弹出框 -->
                <el-popover placement="right-start" width="600" trigger="click">
                  <center>
                    <i class="el-icon-share success"></i>
                    <span type="success">{{scope.row.name}}-来源- {{scope.row.news_nums}} 条新闻</span>
                  </center>
                      <el-table :data="newsData" :highlight-current-row="true"   max-height="250">
                          <el-table-column width="150" property="id" label="编号" fixed align="center"></el-table-column>
                          <el-table-column width="150" property="title" label="标题" fixed align="center"></el-table-column>
                          <el-table-column width="150" property="source" label="来源" align="center"></el-table-column>
                          <el-table-column width="150" label="操作" align="center">
                                      <template slot-scope="scope">
                      
                                  <el-button
                                    size="mini"
                                    type="primary"
                                   ><a target="_blank" rel="noopener noreferrer" :href="scope.row.link" style="color:#fff;text-decoration:none">查看</a></el-button>
                                </template>
                          </el-table-column>

               
              </el-table>

                  <span slot="reference" @click="newsList('Company', scope.row.name)">新闻<el-tag type='danger' size="medium" style="margin: 0 5px"><a>{{ scope.row.news_nums}}</a></el-tag></span>
                </el-popover>
              </template>
            </el-table-column>
            <el-table-column prop="operation" label="标注">
              <template slot-scope="scope">
                <el-button type="info" size="mini" @click="delCompany(scope.row.name)">丢弃</el-button>

                <!-- 弹出框 -->
                <el-popover placement="bottom" width="400" trigger="click" @show="openPopover(scope.row.name)" @hide="hidePopover">

          <center>
            <i class="el-icon-share success"></i>
            <span type="success">同义词</span>
          </center>
          <el-table :data="synonymData" :highlight-current-row="true">
            <el-table-column width="150" property="name" label="同义词"></el-table-column>
            <el-table-column label="操作">
              <template slot-scope="scope">
                        <el-button
                          size="mini"
                          @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
                        <el-button
                          size="mini"
                          type="danger"
                          @click="handleDelete(scope.$index, scope.row)">删除</el-button>
                      </template>
            </el-table-column>
          </el-table>

                <el-button type="warning" size="mini" slot="reference"  @click="getCompanySyn(scope.row.name)">企业同义词</el-button>
        </el-popover>

        <!-- 弹出框 -->
                <el-popover placement="bottom" width="400" trigger="click" @show="openPopover(scope.row.name)" @hide="hidePopover">

                  <center>
                    <el-button type="success" size="mini"><i class="el-icon-circle-plus"></i><span type="success">新公司实体</span></el-button>
                  </center>
                  <div class="demo-input-suffix">
                    公司
                  <el-input v-model="input_company" placeholder="公司全称" type="textarea" autosize></el-input>
                  </div>
                  
                  <div class="demo-input-suffix">
                    公司同义词
                  <el-input v-model="input_company_syn" type="textarea" placeholder="同义词 每行一条"></el-input>
                      <center>
                    <div id="add_company_syn">
                      <el-button type="success" @click="addCompany(scope.row.name)">添加</el-button>
                    </div>
                    </center>
                    </div>
                <el-button type="success" slot="reference" size="mini" >新企业实体</el-button>
                </el-popover>
              </template>
            </el-table-column>
          </el-table>
        </template>

        <template v-else-if="showTable === 'RelationTable'">
          <el-table :data="tableData" key="RelationTable">
            <el-table-column prop="keyword" label="新闻来源" width="140">
              <template slot-scope="scope">
               <span>{{ scope.row.news_id }} 等<el-tag type='danger' size="mini" style="margin: 0 5px">{{scope.row.news_nums}}</el-tag></span>
              </template>
            </el-table-column>
            <el-table-column prop="title" label="新闻标题" >
              <template slot-scope="scope">
                <span>{{ scope.row.news_title}}</span>
              </template>
            </el-table-column>
            <el-table-column prop="invest" label="投资方" >
              <template slot-scope="scope">
                <span>{{ scope.row.invest}}</span>
              </template>
            </el-table-column>
            <el-table-column prop="investR" label="投资关系" >
              <template slot-scope="scope">
                <span>{{ scope.row.level }}</span>
              </template>
            </el-table-column>
             <el-table-column prop="invested" label="融资方" >
              <template slot-scope="scope">
                <span>{{ scope.row.invested}}</span>
              </template>
            </el-table-column>
            <el-table-column prop="operation" label="标注">
              <template slot-scope="scope">
                <el-button type="primary" size="mini" >确认</el-button>
                <el-button type="warning" size="mini">修正</el-button>
              </template>
            </el-table-column>
          </el-table>
        </template>
      </el-main>

    </el-container>
</el-container>

</div>
</template>

<script>
export default {
  data() {
    const item = {
      keyword: "图像识别"
    };
    return {
      axios: require("axios"),
      msg: "hello",
      tableData: [],
      newsData: [],
      patentData: [],
      showTable: "TechTable",
      patent_nums: 30,
      root_url: "http://localhost:8000/",
      company_list_url: "http://localhost:8000/" + "company_list_ajax",
      tech_list_url: "http://localhost:8000/" + "tech_list_ajax",
      finance_list_url: "http://localhost:8000/" + "finance_list_ajax",

      // popover
      synonymData: [{ name: "jd" }, { name: "狗东" }],
      input_company: "",
      input_company_syn: ""
    };
  },
  computed: {
    rmsg: function() {
      return this.msg
        .split("")
        .reverse()
        .join("");
    }
  },
  mounted() {
    this.getTech();
    // this.axios.defaults.xsrfHeaderName = "X-CSRFToken";
  },
  methods: {
    setShowTable(showTable) {
      this.showTable = showTable;
      if (showTable === "TechTable") {
        console.log("toggle TechTable");
        this.getTech();
      }
      if (showTable === "CompanyTable") {
        console.log("toggle companyTable");
        this.getCompany();
      }
      if (showTable === "RelationTable") {
        console.log("toggle RelationTable");
        this.getFinance();
      }
    },
    open() {
      this.$alert("这是一段内容", "标题名称", {
        confirmButtonText: "确定",
        callback: action => {
          this.$message({
            type: "info",
            message: `action: ${action}`
          });
        }
      });
    },

    newsList(type, kw) {
      // ajax request
      console.log("news display....", kw);
      if (type === "Company") {
        var ajax_url = this.root_url + "news_company_list_ajax/" + kw;
      }
      if (type === "Tech") {
        var ajax_url = this.root_url + "news_tech_list_ajax/" + kw;
      }
      this.axios.get(ajax_url).then(response => {
        console.log(response.data.news);
        this.newsData = response.data.news;
      });
    },

    patentList(kw) {
      var ajax_url = this.root_url + "patent_list_ajax/" + kw;
      this.axios.get(ajax_url).then(response => {
        console.log(response.data.patents);
        this.patentData = response.data.patents;
      });
    },
    getCompany() {
      console.log("here is getCompany");

      this.axios.get(this.company_list_url).then(response => {
        console.log("in axios ajax");
        console.log("raw res", response);
        var companys = response.data.companys;
        this.tableData = companys;
        console.log("get the res!");
      });
    },

    getTech() {
      console.log("in getTech");
      this.axios.get(this.tech_list_url).then(response => {
        console.log("in axios ajax");
        console.log("raw res", response);
        var techs = response.data.techs;
        this.tableData = techs;
        console.log("get the res!");
      });
    },
    getFinance() {
      console.log("in getFinance");
      this.axios.get(this.finance_list_url).then(response => {
        console.log("in axios ajax");
        console.log("raw res", response);
        var finance = response.data.finance;
        this.tableData = finance;
        console.log("get the res!");
      });
    },

    getCompanySyn(company) {
      console.log("in getcs");
      var ajax_url = this.root_url + "company_synonym_list/" + company;
      this.axios.get(ajax_url).then(response => {
        this.synonymData = response.data.company_synonym;
      });
    },
    getTechSyn(tech) {
      var ajax_url = this.root_url + "tech_synonym_list/" + tech;
      this.axios.get(ajax_url).then(response => {
        this.synonymData = response.data.tech_synonym;
        this.showPoper = true;
      });
    },
    // --------- delete------------------
    delCompany(name) {
      console.log("in delCompany", name);
      var ajax_url = this.root_url + "keywords_company/delete/" + name;
      this.$confirm("确认删除?", "企业关键词: " + name, {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning"
      })
        .then(() => {
          this.axiosGet(ajax_url, name);
          this.$message({
            type: "success",
            message: "删除成功"
          });
        })
        .catch(() => {
          this.$message({
            type: "info",
            message: "已取消删除"
          });
        });
      //   callback: action => {
      //     this.axiosGet(ajax_url, name);
      //   }
      // });
    },
    delTech(name) {
      console.log("in delTech", name);
      var ajax_url = this.root_url + "keywords_tech/delete/" + name;
      this.$confirm("确认删除?", "技术关键词: " + name, {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning"
      })
        .then(() => {
          this.axiosGet(ajax_url, name);
          this.$message({
            type: "success",
            message: "删除成功"
          });
        })
        .catch(() => {
          this.$message({
            type: "info",
            message: "已取消删除"
          });
        });
    },

    //  ---------------------  add ----------------------------
    addCompany(kw) {
      var name = this.input_company;
      var company_syn = this.input_company_syn.split("\n");
      var ajax_url = this.root_url + "company/add/" + name;
      console.log("the add url:", ajax_url);
      var data = {
        kw: kw,
        company_syn: company_syn
      };
      this.axios({
        method: "POST",
        url: ajax_url,
        data: data
        // transformRequest: [
        //   function(data) {
        //     let ret = "";
        //     for (let it in data) {
        //       ret +=
        //         encodeURIComponent(it) +
        //         "=" +
        //         encodeURIComponent(data[it]) +
        //         "&";
        //     }
        //     return ret;
        //   }
        // ]
      }).then(response => {
        console.log("the add res", response);
        console.log("the add res state", response.data.state);
        this.showMsg(response.data.state, "添加");
        //标注完成 消除显示
      });
    },

    axiosGet(ajax_url, msg) {
      console.log("[axiosGet]::msg:", msg);
      this.axios.get(ajax_url).then(response => {
        console.log("in axios ajax");
        console.log("raw res", response);
        var state = response.data.state;
        console.log("get the res!");
        this.cb(state, msg);
      });
    },

    axiosPost(ajax_url, data) {
      this.axios.post(ajax_url, data).then(response => {
        console.log("in axios ajax");
        console.log("raw res", response);
        console.log("get the res!");
      });
    },

    showMsg(state, msg) {
      console.log("[showMsg]::state ", state);
      if (state === "success") {
        this.$message({
          type: "success",
          message: msg + "成功"
        });
        // this.getCompany();
      } else {
        this.$message({
          type: "error",
          message: msg + "失败"
        });
      }
    },

    cb(state, msg) {
      console.log("in cb msg:", msg);
      console.log("in cb state:", state);
      this.showMsg(state, "删除" + "[" + msg + "]");
      console.log("state:", state);
      if (state === "success") {
        this.getCompany();
      }
    },
    openPopover(name) {
      console.log("open over");
      this.input_company = name;
    },
    hidePopover() {
      console.log("close over");
      this.input_company = "";
      this.input_company_syn = "";
    },
    handleEdit(index, row) {
      console.log(index, row);
    },
    handleDelete(index, row) {
      console.log(index, row);
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.el-header {
  background-color: #24292e;
  color: #fff;
  height: 50px;
  line-height: 50px;
  text-align: left;
}
.el-main {
  padding: 30px;
}
.el-textarea {
  margin-top: 10px;
  margin-bottom: 10px;
}
.el-tag {
  cursor: pointer;
}

#add_company_syn {
  margin-top: 20px;
}
</style>
