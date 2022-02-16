import streamlit as st
import streamlit.components.v1 as components


def clock():
    #Add the html

    components.html("""<!--Dayspedia.com widget--><div class="DPDC" cityid="7842" lang="en" id="dayspedia_widget_f294843011b85e" host="https://dayspedia.com" ampm="true" nightsign="true" sun="false" style="background-image: url(&quot;https://cdn.dayspedia.com/img/widgets/bg-9.png&quot;);">

	<style media="screen" id="dayspedia_widget_f294843011b85e_style">
				/*COMMON*/
		.DPDC{display:table;position:relative;box-sizing:border-box;font-size:100.01%;font-style:normal;font-family:Arial;background-position:50% 50%;background-repeat:no-repeat;background-size:cover;overflow:hidden;user-select:none}
		.DPDCh,.DPDCd{width:fit-content;line-height:1.4}
		.DPDCh{margin-bottom:1em}
		.DPDCd{margin-top:.24em}
		.DPDCt{line-height:1}
		.DPDCth,.DPDCtm,.DPDCts{display:inline-block;vertical-align:text-top;white-space:nowrap}
		.DPDCth{min-width:1.15em}
		.DPDCtm,.DPDCts{min-width:1.44em}
		.DPDCtm::before,.DPDCts::before{display:inline-block;content:':';vertical-align:middle;margin:-.34em 0 0 -.07em;width:.32em;text-align:center;opacity:.72;filter:alpha(opacity=72)}
		.DPDCt12{display:inline-block;vertical-align:text-top;font-size:40%}
		.DPDCdm::after{content:' '}
		.DPDCda::after{content:', '}
		.DPDCdt{margin-right:.48em}
		.DPDCtn{display:inline-block;position:relative;width:13px;height:13px;border:2px solid;border-radius:50%;overflow:hidden}
		.DPDCtn>i{display:block;content:'';position:absolute;right:33%;top:-5%;width:85%;height:85%;border-radius:50%}
		.DPDCs{margin:.96em 0 0 -3px;font-size:90%;line-height:1;white-space:nowrap}
		.DPDCs sup{padding-left:.24em;font-size:65%}
		.DPDCsl::before,.DPDCsl::after{display:inline-block;opacity:.4}
		.DPDCsl::before{content:'~';margin:0 .12em}
		.DPDCsl::after{content:'~';margin:0 .24em}
		.DPDCs svg{display:inline-block;vertical-align:bottom;width:1.2em;height:1.2em;opacity:.48}
		/*CUSTOM*/
		
		.DPDC{width:auto;padding:24px;background-color:#ffffff;border:1px solid #343434;border-radius:8px} /* widget width, padding, background, border, rounded corners */
		.DPDCh{color:#007DBF;font-weight:normal} /* headline color, font-weight*/
		.DPDCt,.DPDCd{color:#343434;font-weight:bold} /* time & date color, font-weight */
		.DPDCtn{border-color:#343434} /* night-sign color = time & date color */
		.DPDCtn>i{background-color:#343434} /* night-sign color = time & date color */
		.DPDCt{font-size:48px} /* time font-size */
		.DPDCh,.DPDCd{font-size:16px} /* headline & date font-size */
	</style>

	<a class="DPl" href="https://dayspedia.com/time/vn/Ho_Chi_Minh_City/" target="_blank" style="display:block!important;text-decoration:none!important;border:none!important;cursor:pointer!important;background:transparent!important;line-height:0!important;text-shadow:none!important;position:absolute;z-index:1;top:0;right:0;bottom:0;left:0">
		<svg xmlns="http://www.w3.org/2000/svg" viewbox="0 0 16 16" style="position:absolute;right:8px;bottom:0;width:16px;height:16px">
			<path style="fill: rgb(255, 165, 125);" d="M0,0v16h1.7c-0.1-0.2-0.1-0.3-0.1-0.5c0-0.9,0.8-1.6,1.6-1.6c0.9,0,1.6,0.8,1.6,1.6c0,0.2,0,0.3-0.1,0.5h1.8 c-0.1-0.2-0.1-0.3-0.1-0.5c0-0.9,0.8-1.6,1.6-1.6s1.6,0.8,1.6,1.6c0,0.2,0,0.3-0.1,0.5h1.8c-0.1-0.2-0.1-0.3-0.1-0.5 c0-0.9,0.8-1.6,1.6-1.6c0.9,0,1.6,0.8,1.6,1.6c0,0.2,0,0.3-0.1,0.5H16V0H0z M4.2,8H2V2h2.2c2.1,0,3.3,1.3,3.3,3S6.3,8,4.2,8z M11.4,6.3h-0.8V8H9V2h2.5c1.4,0,2.4,0.8,2.4,2.1C13.9,5.6,12.9,6.3,11.4,6.3z M4.4,3.5H3.7v3h0.7C5.4,6.5,6,6,6,5 C6,4.1,5.4,3.5,4.4,3.5z M11.3,3.4h-0.8V5h0.8c0.6,0,0.9-0.3,0.9-0.8C12.2,3.7,11.9,3.4,11.3,3.4z">
			</path>
		</svg>
		<span title="DaysPedia.com" style="position: absolute; right: 28px; bottom: 6px; height: 10px; width: 60px; overflow: hidden; text-align: right; color: rgb(255, 165, 125); font-style: normal !important; font-variant-caps: normal !important; font-weight: normal !important; font-stretch: normal !important; font-size: 10px !important; line-height: 10px !important; font-family: Arial, sans-serif !important;">Powered&nbsp;by DaysPedia.com</span>
	</a>
	<div class="DPDCh" style="color: rgb(255, 165, 125);">Current Time in Ho Chi Minh City</div>
	<div class="DPDCt" style="color: rgb(255, 226, 214); font-weight: bold;">
		<span class="DPDCth">05</span><span class="DPDCtm">21</span><span class="DPDCts">37</span><span class="DPDCt12">pm</span>
	</div>
	<div class="DPDCd" style="color: rgb(255, 226, 214); font-weight: bold;">
		<span class="DPDCdt">Wed, February 16</span><span class="DPDCtn" style="display: none; border-color: rgb(255, 226, 214);"><i style="background-color: rgb(255, 226, 214);"></i></span>
	</div>
	
	<div class="DPDCs" style="display: none; color: rgb(255, 226, 214);">
		<span class="DPDCsr">
			<svg xmlns="http://www.w3.org/2000/svg" viewbox="0 0 24 24"><path d="M12,4L7.8,8.2l1.4,1.4c0,0,0.9-0.9,1.8-1.8V14h2c0,0,0-3.3,0-6.2l1.8,1.8l1.4-1.4L12,4z" style="fill: rgb(255, 226, 214);"></path><path d="M6.8,15.3L5,13.5l-1.4,1.4l1.8,1.8L6.8,15.3z M4,21H1v2h3V21z M20.5,14.9L19,13.5l-1.8,1.8l1.4,1.4L20.5,14.9z M20,21v2h3 v-2H20z M6.1,23C6,22.7,6,22.3,6,22c0-3.3,2.7-6,6-6s6,2.7,6,6c0,0.3,0,0.7-0.1,1H6.1z" style="fill: rgb(255, 226, 214);"></path></svg>
			06:13<sup>am</sup>
		</span>
		<span class="DPDCsl">11:48</span>
		<span class="DPDCss">
			<svg xmlns="http://www.w3.org/2000/svg" viewbox="0 0 24 24"><path d="M12,14L7.8,9.8l1.4-1.4c0,0,0.9,0.9,1.8,1.8V4h2c0,0,0,3.3,0,6.2l1.8-1.8l1.4,1.4L12,14z" style="fill: rgb(255, 226, 214);"></path><path d="M6.8,15.3L5,13.5l-1.4,1.4l1.8,1.8L6.8,15.3z M4,21H1v2h3V21z M20.5,14.9L19,13.5l-1.8,1.8l1.4,1.4L20.5,14.9z M20,21v2h3 v-2H20z M6.1,23C6,22.7,6,22.3,6,22c0-3.3,2.7-6,6-6s6,2.7,6,6c0,0.3,0,0.7-0.1,1H6.1z" style="fill: rgb(255, 226, 214);"></path></svg>
			06:01<sup>pm</sup>
		</span>
	</div>
	<script>
		var s, t; s = document.createElement("script"); s.type = "text/javascript";
		s.src = "//cdn.dayspedia.com/js/dwidget.min.v7c6abcf8.js";
		t = document.getElementsByTagName('script')[0]; t.parentNode.insertBefore(s, t);
		s.onload = function() {
			window.dwidget = new window.DigitClock();
			window.dwidget.init("dayspedia_widget_f294843011b85e");
		};
	</script>
	<!--/DPDC-->
	</div><!--Dayspedia.com widget ENDS-->""", height=350)
def Homepage():
    Home_sidebar()
    Home_body()

def Home_sidebar():
    st.sidebar.write("""
    #### Some of my works: \n
    [Github](https://github.com/hungha11) \n
    [LinkedIn](https://www.linkedin.com/in/quốc-hùng-hà-6b192b222/)\n
    [Facebook](https://www.facebook.com/ha.quoc.hung11)
    """)




def Home_body():
    st.write('##### Some of the information about myself:')
    st.write("""
    I am a student at RMIT University in Vietnam. \n
    With the enthusiasm of learning new things, I am always looking for new challenges. \n
    Although my major is Economics and Finance, I am also interested in Machine Learning and Data Science, 
    especially its application in Algorithmic Trading. \n 
    I am a self-taught programmer and I am always trying to improve my skills. Additionally, you can contact me at: \n
        qhung9621@gmail.com
        
    #
    #
    """)

    st.write("""
    ##### About this project: \n
    The purpose of this project is to be the place that I can store my projects and share them with others. \n
    Currently, there are two big parts, which is Streamlit and Algorithmic Trading code.
    I hope in the near future, I can fill the Machine Learning and Statistics page.   \n
    ***
    The project is written in python and built on the Streamlit framework. \n
    Some of the interesting libraries that I used are: \n
    - For data source:
        - [vnquant](https://github.com/phamdinhkhanh/vnquant) \n
        - [investpy](https://investpy.readthedocs.io)
    - For plotting:
        - [plotly](https://plot.ly/python/) \n
        - [mplfinance](https://github.com/matplotlib/mplfinance) \n
    """)
    clock()