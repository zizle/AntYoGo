//index.js
//获取应用实例
const app = getApp()

//Page Object
Page({
  data: {
    
  },
  //options(Object)
  onLoad: function(options) {
    var reqTask = wx.request({
      url: app.globalData.serverHost + "home/swiperdata/",
      data: {},
      header: {'content-type':'application/json'},
      method: 'GET',
      dataType: 'json',
      responseType: 'text',
      success: (result) => {
        
      },
      fail: () => {},
      complete: () => {}
    });
      
  },
  onReady: function() {
    
  },
  onShow: function() {
    
  },
  onHide: function() {

  },
  onUnload: function() {

  },
  onPullDownRefresh: function() {

  },
  onReachBottom: function() {

  },
  onShareAppMessage: function() {

  },
  onPageScroll: function() {

  },
  //item(index,pagePath,text)
  onTabItemTap:function(item) {

  }
});
  
