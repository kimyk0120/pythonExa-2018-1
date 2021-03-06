{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>기간</th>\n",
       "      <th>자치구</th>\n",
       "      <th>세대</th>\n",
       "      <th>인구</th>\n",
       "      <th>인구.1</th>\n",
       "      <th>인구.2</th>\n",
       "      <th>인구.3</th>\n",
       "      <th>인구.4</th>\n",
       "      <th>인구.5</th>\n",
       "      <th>인구.6</th>\n",
       "      <th>인구.7</th>\n",
       "      <th>인구.8</th>\n",
       "      <th>세대당인구</th>\n",
       "      <th>65세이상고령자</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>기간</td>\n",
       "      <td>자치구</td>\n",
       "      <td>세대</td>\n",
       "      <td>합계</td>\n",
       "      <td>합계</td>\n",
       "      <td>합계</td>\n",
       "      <td>한국인</td>\n",
       "      <td>한국인</td>\n",
       "      <td>한국인</td>\n",
       "      <td>등록외국인</td>\n",
       "      <td>등록외국인</td>\n",
       "      <td>등록외국인</td>\n",
       "      <td>세대당인구</td>\n",
       "      <td>65세이상고령자</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>기간</td>\n",
       "      <td>자치구</td>\n",
       "      <td>세대</td>\n",
       "      <td>계</td>\n",
       "      <td>남자</td>\n",
       "      <td>여자</td>\n",
       "      <td>계</td>\n",
       "      <td>남자</td>\n",
       "      <td>여자</td>\n",
       "      <td>계</td>\n",
       "      <td>남자</td>\n",
       "      <td>여자</td>\n",
       "      <td>세대당인구</td>\n",
       "      <td>65세이상고령자</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2018.2/4</td>\n",
       "      <td>합계</td>\n",
       "      <td>4241547</td>\n",
       "      <td>10089517</td>\n",
       "      <td>4935944</td>\n",
       "      <td>5153573</td>\n",
       "      <td>9814049</td>\n",
       "      <td>4802769</td>\n",
       "      <td>5011280</td>\n",
       "      <td>275468</td>\n",
       "      <td>133175</td>\n",
       "      <td>142293</td>\n",
       "      <td>2.31</td>\n",
       "      <td>1393671</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2018.2/4</td>\n",
       "      <td>종로구</td>\n",
       "      <td>73655</td>\n",
       "      <td>163569</td>\n",
       "      <td>79522</td>\n",
       "      <td>84047</td>\n",
       "      <td>153780</td>\n",
       "      <td>75247</td>\n",
       "      <td>78533</td>\n",
       "      <td>9789</td>\n",
       "      <td>4275</td>\n",
       "      <td>5514</td>\n",
       "      <td>2.09</td>\n",
       "      <td>26512</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2018.2/4</td>\n",
       "      <td>중구</td>\n",
       "      <td>61091</td>\n",
       "      <td>135427</td>\n",
       "      <td>66673</td>\n",
       "      <td>68754</td>\n",
       "      <td>126032</td>\n",
       "      <td>62260</td>\n",
       "      <td>63772</td>\n",
       "      <td>9395</td>\n",
       "      <td>4413</td>\n",
       "      <td>4982</td>\n",
       "      <td>2.06</td>\n",
       "      <td>21798</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>2018.2/4</td>\n",
       "      <td>용산구</td>\n",
       "      <td>108516</td>\n",
       "      <td>245245</td>\n",
       "      <td>119963</td>\n",
       "      <td>125282</td>\n",
       "      <td>229677</td>\n",
       "      <td>111078</td>\n",
       "      <td>118599</td>\n",
       "      <td>15568</td>\n",
       "      <td>8885</td>\n",
       "      <td>6683</td>\n",
       "      <td>2.12</td>\n",
       "      <td>37331</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>2018.2/4</td>\n",
       "      <td>성동구</td>\n",
       "      <td>135666</td>\n",
       "      <td>316068</td>\n",
       "      <td>155268</td>\n",
       "      <td>160800</td>\n",
       "      <td>308066</td>\n",
       "      <td>151571</td>\n",
       "      <td>156495</td>\n",
       "      <td>8002</td>\n",
       "      <td>3697</td>\n",
       "      <td>4305</td>\n",
       "      <td>2.27</td>\n",
       "      <td>42171</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>2018.2/4</td>\n",
       "      <td>광진구</td>\n",
       "      <td>161294</td>\n",
       "      <td>370519</td>\n",
       "      <td>179621</td>\n",
       "      <td>190898</td>\n",
       "      <td>355748</td>\n",
       "      <td>173216</td>\n",
       "      <td>182532</td>\n",
       "      <td>14771</td>\n",
       "      <td>6405</td>\n",
       "      <td>8366</td>\n",
       "      <td>2.21</td>\n",
       "      <td>44806</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>2018.2/4</td>\n",
       "      <td>동대문구</td>\n",
       "      <td>160757</td>\n",
       "      <td>364527</td>\n",
       "      <td>180126</td>\n",
       "      <td>184401</td>\n",
       "      <td>348903</td>\n",
       "      <td>174128</td>\n",
       "      <td>174775</td>\n",
       "      <td>15624</td>\n",
       "      <td>5998</td>\n",
       "      <td>9626</td>\n",
       "      <td>2.17</td>\n",
       "      <td>56675</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>2018.2/4</td>\n",
       "      <td>중랑구</td>\n",
       "      <td>179690</td>\n",
       "      <td>410296</td>\n",
       "      <td>203711</td>\n",
       "      <td>206585</td>\n",
       "      <td>405551</td>\n",
       "      <td>201803</td>\n",
       "      <td>203748</td>\n",
       "      <td>4745</td>\n",
       "      <td>1908</td>\n",
       "      <td>2837</td>\n",
       "      <td>2.26</td>\n",
       "      <td>60618</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>2018.2/4</td>\n",
       "      <td>성북구</td>\n",
       "      <td>186696</td>\n",
       "      <td>451829</td>\n",
       "      <td>218998</td>\n",
       "      <td>232831</td>\n",
       "      <td>440272</td>\n",
       "      <td>214430</td>\n",
       "      <td>225842</td>\n",
       "      <td>11557</td>\n",
       "      <td>4568</td>\n",
       "      <td>6989</td>\n",
       "      <td>2.36</td>\n",
       "      <td>67132</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>2018.2/4</td>\n",
       "      <td>강북구</td>\n",
       "      <td>143187</td>\n",
       "      <td>326063</td>\n",
       "      <td>159219</td>\n",
       "      <td>166844</td>\n",
       "      <td>322385</td>\n",
       "      <td>157769</td>\n",
       "      <td>164616</td>\n",
       "      <td>3678</td>\n",
       "      <td>1450</td>\n",
       "      <td>2228</td>\n",
       "      <td>2.25</td>\n",
       "      <td>57401</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>2018.2/4</td>\n",
       "      <td>도봉구</td>\n",
       "      <td>137560</td>\n",
       "      <td>344096</td>\n",
       "      <td>168282</td>\n",
       "      <td>175814</td>\n",
       "      <td>341928</td>\n",
       "      <td>167465</td>\n",
       "      <td>174463</td>\n",
       "      <td>2168</td>\n",
       "      <td>817</td>\n",
       "      <td>1351</td>\n",
       "      <td>2.49</td>\n",
       "      <td>54969</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>2018.2/4</td>\n",
       "      <td>노원구</td>\n",
       "      <td>217662</td>\n",
       "      <td>553177</td>\n",
       "      <td>268396</td>\n",
       "      <td>284781</td>\n",
       "      <td>549365</td>\n",
       "      <td>266826</td>\n",
       "      <td>282539</td>\n",
       "      <td>3812</td>\n",
       "      <td>1570</td>\n",
       "      <td>2242</td>\n",
       "      <td>2.52</td>\n",
       "      <td>75741</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>2018.2/4</td>\n",
       "      <td>은평구</td>\n",
       "      <td>203547</td>\n",
       "      <td>489045</td>\n",
       "      <td>236802</td>\n",
       "      <td>252243</td>\n",
       "      <td>484642</td>\n",
       "      <td>234905</td>\n",
       "      <td>249737</td>\n",
       "      <td>4403</td>\n",
       "      <td>1897</td>\n",
       "      <td>2506</td>\n",
       "      <td>2.38</td>\n",
       "      <td>76097</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>2018.2/4</td>\n",
       "      <td>서대문구</td>\n",
       "      <td>137725</td>\n",
       "      <td>323261</td>\n",
       "      <td>154145</td>\n",
       "      <td>169116</td>\n",
       "      <td>311280</td>\n",
       "      <td>150131</td>\n",
       "      <td>161149</td>\n",
       "      <td>11981</td>\n",
       "      <td>4014</td>\n",
       "      <td>7967</td>\n",
       "      <td>2.26</td>\n",
       "      <td>49935</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>2018.2/4</td>\n",
       "      <td>마포구</td>\n",
       "      <td>170788</td>\n",
       "      <td>385507</td>\n",
       "      <td>182627</td>\n",
       "      <td>202880</td>\n",
       "      <td>374691</td>\n",
       "      <td>178430</td>\n",
       "      <td>196261</td>\n",
       "      <td>10816</td>\n",
       "      <td>4197</td>\n",
       "      <td>6619</td>\n",
       "      <td>2.19</td>\n",
       "      <td>50350</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>2018.2/4</td>\n",
       "      <td>양천구</td>\n",
       "      <td>176234</td>\n",
       "      <td>471026</td>\n",
       "      <td>232087</td>\n",
       "      <td>238939</td>\n",
       "      <td>467151</td>\n",
       "      <td>230322</td>\n",
       "      <td>236829</td>\n",
       "      <td>3875</td>\n",
       "      <td>1765</td>\n",
       "      <td>2110</td>\n",
       "      <td>2.65</td>\n",
       "      <td>56742</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>2018.2/4</td>\n",
       "      <td>강서구</td>\n",
       "      <td>256560</td>\n",
       "      <td>606981</td>\n",
       "      <td>295221</td>\n",
       "      <td>311760</td>\n",
       "      <td>600257</td>\n",
       "      <td>291966</td>\n",
       "      <td>308291</td>\n",
       "      <td>6724</td>\n",
       "      <td>3255</td>\n",
       "      <td>3469</td>\n",
       "      <td>2.34</td>\n",
       "      <td>78042</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>2018.2/4</td>\n",
       "      <td>구로구</td>\n",
       "      <td>171882</td>\n",
       "      <td>440305</td>\n",
       "      <td>220880</td>\n",
       "      <td>219425</td>\n",
       "      <td>407235</td>\n",
       "      <td>202016</td>\n",
       "      <td>205219</td>\n",
       "      <td>33070</td>\n",
       "      <td>18864</td>\n",
       "      <td>14206</td>\n",
       "      <td>2.37</td>\n",
       "      <td>60564</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>2018.2/4</td>\n",
       "      <td>금천구</td>\n",
       "      <td>106307</td>\n",
       "      <td>252752</td>\n",
       "      <td>129612</td>\n",
       "      <td>123140</td>\n",
       "      <td>233263</td>\n",
       "      <td>118530</td>\n",
       "      <td>114733</td>\n",
       "      <td>19489</td>\n",
       "      <td>11082</td>\n",
       "      <td>8407</td>\n",
       "      <td>2.19</td>\n",
       "      <td>34945</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>2018.2/4</td>\n",
       "      <td>영등포구</td>\n",
       "      <td>169264</td>\n",
       "      <td>404501</td>\n",
       "      <td>203696</td>\n",
       "      <td>200805</td>\n",
       "      <td>369003</td>\n",
       "      <td>183888</td>\n",
       "      <td>185115</td>\n",
       "      <td>35498</td>\n",
       "      <td>19808</td>\n",
       "      <td>15690</td>\n",
       "      <td>2.18</td>\n",
       "      <td>54994</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>2018.2/4</td>\n",
       "      <td>동작구</td>\n",
       "      <td>174427</td>\n",
       "      <td>407275</td>\n",
       "      <td>197984</td>\n",
       "      <td>209291</td>\n",
       "      <td>394788</td>\n",
       "      <td>192296</td>\n",
       "      <td>202492</td>\n",
       "      <td>12487</td>\n",
       "      <td>5688</td>\n",
       "      <td>6799</td>\n",
       "      <td>2.26</td>\n",
       "      <td>58133</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>2018.2/4</td>\n",
       "      <td>관악구</td>\n",
       "      <td>259681</td>\n",
       "      <td>521960</td>\n",
       "      <td>262235</td>\n",
       "      <td>259725</td>\n",
       "      <td>504048</td>\n",
       "      <td>253600</td>\n",
       "      <td>250448</td>\n",
       "      <td>17912</td>\n",
       "      <td>8635</td>\n",
       "      <td>9277</td>\n",
       "      <td>1.94</td>\n",
       "      <td>71317</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>2018.2/4</td>\n",
       "      <td>서초구</td>\n",
       "      <td>174268</td>\n",
       "      <td>443989</td>\n",
       "      <td>212679</td>\n",
       "      <td>231310</td>\n",
       "      <td>439844</td>\n",
       "      <td>210596</td>\n",
       "      <td>229248</td>\n",
       "      <td>4145</td>\n",
       "      <td>2083</td>\n",
       "      <td>2062</td>\n",
       "      <td>2.52</td>\n",
       "      <td>54614</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25</th>\n",
       "      <td>2018.2/4</td>\n",
       "      <td>강남구</td>\n",
       "      <td>229160</td>\n",
       "      <td>551888</td>\n",
       "      <td>264332</td>\n",
       "      <td>287556</td>\n",
       "      <td>546952</td>\n",
       "      <td>261815</td>\n",
       "      <td>285137</td>\n",
       "      <td>4936</td>\n",
       "      <td>2517</td>\n",
       "      <td>2419</td>\n",
       "      <td>2.39</td>\n",
       "      <td>66011</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>26</th>\n",
       "      <td>2018.2/4</td>\n",
       "      <td>송파구</td>\n",
       "      <td>268325</td>\n",
       "      <td>673161</td>\n",
       "      <td>327051</td>\n",
       "      <td>346110</td>\n",
       "      <td>666439</td>\n",
       "      <td>323741</td>\n",
       "      <td>342698</td>\n",
       "      <td>6722</td>\n",
       "      <td>3310</td>\n",
       "      <td>3412</td>\n",
       "      <td>2.48</td>\n",
       "      <td>79093</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>27</th>\n",
       "      <td>2018.2/4</td>\n",
       "      <td>강동구</td>\n",
       "      <td>177605</td>\n",
       "      <td>437050</td>\n",
       "      <td>216814</td>\n",
       "      <td>220236</td>\n",
       "      <td>432749</td>\n",
       "      <td>214740</td>\n",
       "      <td>218009</td>\n",
       "      <td>4301</td>\n",
       "      <td>2074</td>\n",
       "      <td>2227</td>\n",
       "      <td>2.44</td>\n",
       "      <td>57680</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          기간   자치구       세대        인구     인구.1     인구.2     인구.3     인구.4  \\\n",
       "0         기간   자치구       세대        합계       합계       합계      한국인      한국인   \n",
       "1         기간   자치구       세대         계       남자       여자        계       남자   \n",
       "2   2018.2/4    합계  4241547  10089517  4935944  5153573  9814049  4802769   \n",
       "3   2018.2/4   종로구    73655    163569    79522    84047   153780    75247   \n",
       "4   2018.2/4    중구    61091    135427    66673    68754   126032    62260   \n",
       "5   2018.2/4   용산구   108516    245245   119963   125282   229677   111078   \n",
       "6   2018.2/4   성동구   135666    316068   155268   160800   308066   151571   \n",
       "7   2018.2/4   광진구   161294    370519   179621   190898   355748   173216   \n",
       "8   2018.2/4  동대문구   160757    364527   180126   184401   348903   174128   \n",
       "9   2018.2/4   중랑구   179690    410296   203711   206585   405551   201803   \n",
       "10  2018.2/4   성북구   186696    451829   218998   232831   440272   214430   \n",
       "11  2018.2/4   강북구   143187    326063   159219   166844   322385   157769   \n",
       "12  2018.2/4   도봉구   137560    344096   168282   175814   341928   167465   \n",
       "13  2018.2/4   노원구   217662    553177   268396   284781   549365   266826   \n",
       "14  2018.2/4   은평구   203547    489045   236802   252243   484642   234905   \n",
       "15  2018.2/4  서대문구   137725    323261   154145   169116   311280   150131   \n",
       "16  2018.2/4   마포구   170788    385507   182627   202880   374691   178430   \n",
       "17  2018.2/4   양천구   176234    471026   232087   238939   467151   230322   \n",
       "18  2018.2/4   강서구   256560    606981   295221   311760   600257   291966   \n",
       "19  2018.2/4   구로구   171882    440305   220880   219425   407235   202016   \n",
       "20  2018.2/4   금천구   106307    252752   129612   123140   233263   118530   \n",
       "21  2018.2/4  영등포구   169264    404501   203696   200805   369003   183888   \n",
       "22  2018.2/4   동작구   174427    407275   197984   209291   394788   192296   \n",
       "23  2018.2/4   관악구   259681    521960   262235   259725   504048   253600   \n",
       "24  2018.2/4   서초구   174268    443989   212679   231310   439844   210596   \n",
       "25  2018.2/4   강남구   229160    551888   264332   287556   546952   261815   \n",
       "26  2018.2/4   송파구   268325    673161   327051   346110   666439   323741   \n",
       "27  2018.2/4   강동구   177605    437050   216814   220236   432749   214740   \n",
       "\n",
       "       인구.5    인구.6    인구.7    인구.8  세대당인구  65세이상고령자  \n",
       "0       한국인   등록외국인   등록외국인   등록외국인  세대당인구  65세이상고령자  \n",
       "1        여자       계      남자      여자  세대당인구  65세이상고령자  \n",
       "2   5011280  275468  133175  142293   2.31   1393671  \n",
       "3     78533    9789    4275    5514   2.09     26512  \n",
       "4     63772    9395    4413    4982   2.06     21798  \n",
       "5    118599   15568    8885    6683   2.12     37331  \n",
       "6    156495    8002    3697    4305   2.27     42171  \n",
       "7    182532   14771    6405    8366   2.21     44806  \n",
       "8    174775   15624    5998    9626   2.17     56675  \n",
       "9    203748    4745    1908    2837   2.26     60618  \n",
       "10   225842   11557    4568    6989   2.36     67132  \n",
       "11   164616    3678    1450    2228   2.25     57401  \n",
       "12   174463    2168     817    1351   2.49     54969  \n",
       "13   282539    3812    1570    2242   2.52     75741  \n",
       "14   249737    4403    1897    2506   2.38     76097  \n",
       "15   161149   11981    4014    7967   2.26     49935  \n",
       "16   196261   10816    4197    6619   2.19     50350  \n",
       "17   236829    3875    1765    2110   2.65     56742  \n",
       "18   308291    6724    3255    3469   2.34     78042  \n",
       "19   205219   33070   18864   14206   2.37     60564  \n",
       "20   114733   19489   11082    8407   2.19     34945  \n",
       "21   185115   35498   19808   15690   2.18     54994  \n",
       "22   202492   12487    5688    6799   2.26     58133  \n",
       "23   250448   17912    8635    9277   1.94     71317  \n",
       "24   229248    4145    2083    2062   2.52     54614  \n",
       "25   285137    4936    2517    2419   2.39     66011  \n",
       "26   342698    6722    3310    3412   2.48     79093  \n",
       "27   218009    4301    2074    2227   2.44     57680  "
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.read_excel(\"../data/01_Population_Seoul.xls\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
