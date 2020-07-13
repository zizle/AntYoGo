<template>
<div>
    <Row></Row>
    <Row>
        <Col span="6" offset="9">
            <Card :bordered="true">
                <p slot="title">登录</p>
                <Form ref="formValidate" :model="formValidate" :rules="ruleValidate" :label-width="80">
                    <FormItem label="用户名" prop="username">
                        <Input v-model="formValidate.username" placeholder="用户名"></Input>
                    </FormItem>
                    <FormItem label="密码" prop="password">
                        <Input v-model="formValidate.password" placeholder="密码" type="password" password></Input>
                    </FormItem>
                    <FormItem>
                        <Button type="primary" @click="handleSubmit('formValidate')">登录</Button>
                        <Button @click="handleReset('formValidate')" style="margin-left: 6px">重置</Button>
                    </FormItem>
                </Form>
            </Card>
        </Col>
    </Row>
</div>
</template>
<script>
export default{
    name:"Login",
    data () {
        return {
            formValidate: {
                username: '',
                password: '',
                city: '',
                gender: '',
                interest: [],
                date: '',
                time: '',
                desc: ''
            },
            ruleValidate: {
                username: [
                    { required: true, message: '用户名不能为空', trigger: 'blur' }
                ],
                password: [
                    { required: true, message: '密码不能为空', trigger: 'blur' },
                ],
            },

        }
    },
    methods:{
        handleSubmit (name) {
            this.$refs[name].validate((valid) => {
                if (valid) {
                    this.$Message.success('登录成功!');
                } else {
                    this.$Message.error('失败!');
                }
            })
        },
        handleReset (name) {
            this.$refs[name].resetFields();
        },
    //   toLogin(){
    //       alert("点击了登录");
    //       this.$router.push('/');  // 跳转至后台主页
    //   }
  }
}
</script>
<style scoped>

</style>