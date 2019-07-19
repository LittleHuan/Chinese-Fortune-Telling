# coding=gbk
import sys
import urllib
import requests
import pandas as pd
import re
import ssl
import numpy as np
import time
import xlrd
def xingmingceping(xing,ming):
    ssl._create_default_https_context = ssl._create_unverified_context
    targetURL = "https://www.sheup.com/xingming_dafen.php"
    data={}

    data['xingx'] = xing.encode("gbk")
    data['mingx'] = ming.encode("gbk")
    data['xingmingceshi']='�������Դ��'.encode("gbk")
    #���Զ���dataת���ɱ�׼��ʽ
    data = urllib.parse.urlencode(data).encode('utf-8')
    #�����û�����
    html = urllib.request.urlopen(targetURL, data)

    #��ȡ����������
    rst = html.read().decode('gbk','ignore')
    # print (rst)
    try:
        sancai=(re.findall('�������ã���<font color="red"><strong>(.+?)</strong></font>',rst))[0]
        jixiong=(re.findall('���׷�������<font color="green"><strong>(.+?)</strong></font>',rst))[0]
        mingge=(re.findall('���������<font color="blue">(.+?)</font></p>',rst))[0]
        elseword=(re.findall('\d��+(.+?)<',rst))[:12]
    except IndexError:
        return False
    return [sancai,jixiong,mingge,elseword]


def getname():
    xingnote='�Ǹʸ߸𹢹������������Źȹ˹عܹڹ�����������������ºκͺغں��������軨�������ƻػݻ����������Ƽͼּ��彪�������ý������������' \
         '���ۿ����¿׿ܿ��������������Ͱ԰װذ�����������ϱ߱�����������̲Բ�᯲�����˳��ȳ³ɳ̳ٳس���ҳ��ӴԴ޴�����������µ˵ҵ�󶡶�����' \
         '񼶼�Ŷζ������������ѷ���������������������������������������������������������¡¦¥¬³¹·½����������������ëéð÷����������Īľ' \
         '��������������ţũ��ŷ����������Ƥ��ƽ����������Ǯ������������������ȨȫȽ��������������ɣɳ��������������ʢʦʩʯʱʷ��ˮ������������̸̷̩��������' \
         '����ͯ��Ϳ������Τκ��������������������ϯϰ����������Ф��л��������������Ѧ����������������ҦҶ����������Ӧ����������������ԪԬ����������ղ����' \
         '����֣������ףׯ��������'
    f1='����������������������ĩĭ��ĪĮīĬıĳľ������Ľ������������������������������������Ţ��ţŮůŵ�ŷŸ�����������������嫘���M����������Ʈ��Ƶ��Ʒ�ƽ��ƺƻ��Ƽ���������������������������������ݽ��������������������ǧǪܷǨ�ǥǫ�ǰ���ǮǬǱǭ��ٻ����ǿ��Ǿ����������������������������������������������������������ȫȨȪ����ȺȻȼȽ��������������������������������������F���������������ި������������������������ɣɭɳɯɽɼ���ɺ������������������ۿ������|���������ʤ��ʥ��ʢʫʩʮʯʱʵ������������������������������ˡ����˧˫˪ˬˮ˳˴˸˷��˶��˿˾˼˹������ڡ������������������������̫̩̲̳��̷̶̹�����Ǐ|���������������������������������͡��ͤͥ͢��������ͦ��ͧͬ١ͮͩͭͯ����ͫͳͷͼ;������������ݸ������������������΢ޱΡΪΤΧ��ΨΩάΫΰγέί�������δηξεοκ��������ТФЧЦХг��л����о�����ݷп���нܰ����������������������L��������ڼ���������������������������������ѡ�@����Ѥ�����ѧѩ��޹ѰѮ�����ѶѴѸѷѾ���������������۳��������ܾ������������ٲ�������������������������������������������D�������������سҢ��Ҧ��ҥ��ҡң�������ҫҲұҰҵҶҷ������һ�����tҿҼ���������������������������������߮������������������߽�������������������������������������������נD޲��ܲ��������������������طӢݺ��ӧӣ���ӥӭӯ��ӫӨөӪ�����������Ӯ��ӱӰӳӵӹӺܭ��ӽӾ��ӿ����������������ݯ��������������楫_�����������������������������ٶ������Ԧ������������������Ԣ��ԣ��������عԥԨԪ԰��ԫԭԲԬԮԵܫԴ��ԶԷ���Ը������hԿ������Ծ��Խ�����Ȋu�V�ܿ�������������������������������դհչտ�������������������������������������������������������������������֤ں֡��ֱֲ֥֪֮����־��ۤ��ֿ������������������������������������������ׯ׳״׼׿پ����������������������������������������񽡼�꯽���������������訰��񰶰�����������İ˰װذ������ᱱ���������������ȱ��T���쮱������ϱ�������ٱ������������������������������ƲŲĲɲʲβ���貲ٲݲ�����濲������ƫ`�����̳��˳���������衳���������巳�鴬bة�ɳʳг���̳γȳҳڳس۳ٳ�������财�������˴����������´ʴɴȴǴʹϴ��������ʹ����槴������쵤��������������µĵƵҵ�ݶ�ѵصܵ��馵ٵ�����������ණ�������������Ŷȶ˶ضܶ���䊊����������������������������[���󷽷��ՕP���ŷ����Ƿ��������������������ܽ�����������٤���Ƹո�۸�꽸�������������������ٹ����������ȹ۹��ٹ��������������������Ϻ��ʺ������H�պ�嫺���婺úº�껺ƜB𩰂�尺̺ϺκӺɺغպ׺��������޿����������ݦ��������������������뻴����䡻�徻û����ƻ�諻������Իջܻ���������ݻ�ޥ������������٥���ͼʼ��ü����Ӽ��������μ׼��򽨽���������������������毽�����ٮ���ݽڽܽ����漽��޽�������Q��������誾�桽����ƽ��������ݼ��������������㽾�������溾����������������þ��ͽ۾��پپ��举������������������޿����������B������������������٩����������������ݿÿɿ�㡿�﬿���ӿ������j�����������������������������������������������������������������������������������������������ٳ����۪������ݰ���������������������������������������������������������������������������������������R�������������������������������������¡¤¶³½��¹·º���´���������������������������۽��������ܬ����ëï��öõü÷�������þ��������������������������������������������������ؿ��ẕF��������������������Ϧ��ϫ��ϣ����ۭ���ϧ��ϩ��ϡϪ�����������ϰ��ϲ����Ͽ�ϼ��������������������������������������������������������������������С'
    f21='����˼����С�����һ����������ѩܰ�����紺�����������޺캣���㿡ʫ�������������������������������ȹ������ҵ�����������½�������ӱ�������Ӣ������־���ŷ���Ц�������������ٻ꿿�������������׿�����پ�������������˴��¾���ܿԪ�Ǻ������������ΰ���ݽ���ά¶贫h���������ֺ����������������������ϣӽ˫ܲ�������ӯ������÷�����ֿ�ǧѧܷ����������ޱ�Ө������֥������������о����˹����󰬹�ɺ�Ƕ������ӳ�б��������껰���짽�����������ݼ���������䳯��ƷĽ�������ͮ����������������巿�����ľ�ĺ������������հ������������������������������ʥҶФ֪�����ε�����Խ����ڽ�ӭ��������Բ����Т�ܺ��޲�عнŵ��֮����������ޥ���������ܽ����ӣ��˾���ʾ�Ϫ�����ͤ������ʤ������԰ƽ�B�������������������ԶƼ��Ϧ�����������������ݳ���ʿ����������������ٴϳ���΢Ӿ�����ط���ݳ����������س��Ž������ɯ������˹���������������õ��ٳ����������ϲ˿��ˮ���β��ش�Ψ���������ڿ������������й�Ⱥ����·�t˳ͯ��͢��ʱ�Ǿ����Դ������ʩ�����˸Ϊة����ݷ��ʢ��Է��������������˼���ʮ�ñ�ӱ���չ�غ�����˧������ɼ����诶���غ��ƾ���浶����������������Ժջ�������ϧ�Ķ�ۤ�޸߾����������Ծۿ�ܾ�Τ�����ط�����������߮����˶�ȴ��ɭ��濼��������߾�쳺�����˴ԣ��ϼ��̩ͩ������ī��������½Ƚ�������˻���Ω��ԭ������ϫ����ԥ�������ݸ�Ρ������ҵټ�ͱ������Ĭ����������Ҽ����Ҳ�ƾ����忥���²����M��ݺ�����׳�����������������Ī�ŷǹ�Ȼ�˪������ʯ������͡�ȳ�����ҫ�ҵ�Ԩ�ϕ�����ĭ���Ƴ¼���������̫����ˬ������ҿ��Ң���ױ�����٤�������Ӱ��Ӧ�����������Ȫƻ����������������������ɳ�����ϸ��ȶ��������پ��³����ݸ����ͥδ�Ӳ�������������Կ�������ƻ���泾�����ص���Ч�Ӷ������F�����˲�������ºͬ��Ӯ����襻��������������������������ïǬ�������տ��������ٶ������������∐�����������������������������������ݯ���ѕF��Եѡ����������������ȿ��ܰ���ǰ���о������̲���䭜Bӫ���ë���������������乷������������Ѿ��Ԣ��������˷��������ʦ�������������ϰ�������Ŷ˾�����Х�������۵�婸�𪹫��������έ孱�������������ӧ���д���Ǫ�����������ü´������ڼ����۾���ŷ㡽�������ڡԬ�������������ԦӺ¹��ѵ٥ϡ�������Ѧ�������ڽ�п��������������Ǯ��ɽ��������κ޲��ռ�����όk۪����Ů�������������Ʈ������������̹������ܾ�ط�����Ҧ����������������_¥������ڼ���������½�ö����ڸ�������ر��Lֿ����Ǳ��؟@��Ţ�������țb컷���ʡ��ξ���������������¡�����������ا����������ֺ̼�����������ֶس���¬��Эӵ��������ۼ���ϩ�����ͺ�����������خ��������ο�������������������B�D������뽧ѿ����������׾�������ެ¿����Ҫ�Ӻ������������̷�׵���ҥޭ�����Ϋ����������������������ԫ�ه���������������绯Ǿ�����������㛿���������ղ��ׯ��������֣������پ����������л��������ȫ��������ǫ������������У��殽�v���ǻ����䵭�������쵽�������|��֦��������Ѥ��ۭ�ű�ůʶ��������������������﻾���������Dٮ�����«��ȼ�ֲ��ִ��ң��þ�������ﰥ��ݶ���̶���¾��������䲷��������κ�������ĺ������ܬȰ��ת��٧Ѱ������۴������ױ���椰������ֹ����گ��������������վ�����ؾ��������ި��꽸�����������������T���������üᾯ��ٲ�޹�Ի�����������ʵ��ӡ��Ѹ�����嵩����������ּ�����ľ�����������Ұ������ؿ�V���ܳ��ȼ���֡Լ嵷�������Ļ���������Ի��丰��㲫����佸�ݰ����ԡ����޼γ������ݟ���޿ϯ��쾳۰Բ�������٬H��������ţ��������֤�������᲼߽�������������ӿ������Ϣ����쪻�����ҹ�����������ǥ���������۸ʵ����������ܺ��ӹ��S���̲��ⱱ���༰���������䥸�١�ӷ�ʰ��Ԥ���԰���������������ĵףԸ�͸����Բ���������ҽ��ĩ��Ǩ���ͳ������Į���������׳ܫ��о��ѽ��������յ��̹���Ÿ��䯸�ڱ���ٺ��������¹̷���ڤ����Ѵ����֬����װ�аݻ�����������ظӷڿ������������̳���䱤��ı��ݻί����ݬ����������޹����ֹ�ɣ������հ�Ʒ���ױ�Ӷ�ѭ����ڹݿ�Ӹ������μ�ˡ��ڲ����ꩳ���Ȱ������ǭ�Ժ����տ���Ҭ�������ذ�[���h������������ũ��ب��İ������ʽ����ɺ��u�ջ�޷�䬳������渷ֿ�ר�����谺�����������۳����ͷ�Ƶ�ء����������ĳ���W���䦶���մ�ش�������������������������̦����������Ǣ̸�����Ϯ�������ݮ���������ȸ����䱴��ݹ�����槻����ǳ�ͫ�����������¿����λ�ȱ�����������ȷ�ۥ�����ʨ��������޽Ŀ��ئ�����Ƿ�������ȵ�����ʰ���ݦ��Ӫ������Ĳ��������̳廤�����̫��ԬE�����ע�������Л�����̭��Ѯ�����¼�󰾰�����������˽���鹬����ͭ��Ӥ�ȵ�î���Uȱ��������ѣ�P������Ȩ����آ�����������ݾ�ɷ���˺��켨����ꊊ��������ԯ㺻ر������������������٩������������ǫT����ٹҷ�Ϭ����ϵ����µ����������Ǽڵ�z������ܹ��Ƹͼ�綥�����ƹ��҂m��������г���i���������㿴�����������Ǳ��ʷ����Ժ��Ϥ����Ѷҳ���̳����μ���췴�鶱ө�����ﲭ������������˲������汶���֧�����������ཽ���ҵ���֯����ɴ����ͳ�á������Ѹ�������������ȡ�������Ŵɳ����������㻦������j���ܵ��������q����ұ������޸����Ԯƺ���㻽�о�������ݽ����ѷ��O����ɵ������������ϼ��������������ӳ�|ȥ����������������́�������·����ƼǷ���أ������϶���Ƹ�ƨ�������ݵ������Ũ��ں�ͼ�����׸��������¬g�����Ⱦ�D��ʾ�����Ͳ��塀��Դ��˨������׼�Q������������⻹���а�ϴ��������������������b�Ƕζ��ı�����̶����¤����٣����ֱ�˽��������c�����Ӽ���᪫�����Ư��������˰������������ᳫį��٫�|��������������������ǳ�����Աӥݥ鹷����Ը��������������ؽ����ڭ۫�����C��Ƥ�������ģ������ʼ��᩼�����������������ҜR�ݶ�������ͦ���Խ��������۲���Φ�ļ�������ֵ��ǳ�Կ�������������¢��ƃ�����˶�����������������ݹ������������®�ɺ޲�������������￿���դ��ǡֻ��ܻ��'
    f22='�����ỪȻ��÷������Ӣ������ƽƼͮ�ϼ�����վ�������ӱ�����������������������Ө����������������ܰ���������޾�������褵��������ɺ���骷���������ݷ������ݳ��ؼ�ٻ�����������������ܿ����ޱŵ��ϣ��ѩ������֥����ΰ�㴺һ�����������;�Ԫ�������������������粷�Ƚ���漽��ܺ����Դӯ�������翡��������ܲ¶�����Խ���Գ���Ϫ�������ϫh��ź��𻶺�պ�ݼ�����ɼͩ�����������ûܾ�˼��Ⱥ����ͯ��巺������ݵ���ԲӰЦ���������΢��𩱴����������ε��������ǽ�׿����������ң��ɯ���������������ķ�˫�ɰ�Զ�Ϻ��˶�ά����������Ҷ����ʫƻ�������뱦԰��������ͤ������涬�������B��������������о��������ҢԵɭ濱��ӻ��ɺ����ʴ��溬���翵ľ��ع����ܷϫ��֮���־�����ԭ���Ĳ�Ϊ��������������ʤ��õ�����������Ͻ�������������������вʺ齡������짺�ة��˪�������������ȼ������˽�����������ºޥ����ˮ���������ɽˬ������������������Ͼ���ܽ��ͫ�ӫ���ѧ��͢���������������ӣ�����崨�������ɱ�Ԩ������سʶ���幾������ٺ׿�����ǫ�������Ҿ����������������ʼ���˧��������īԷ���������������ʢ����ϲ��Ρ����˳������ʯ�����͡�ԥʵ����������������������[���������ӿ���ӽ��Ĭ��˸�����������ܻ�����˹����ϦѾ��ҵ���򫶹���������ط�έ�ŵt�߿�Ÿ����޷�ӭ����Ȫ����Կ����������������������������ظ������������������н���氺��������ݽʮ����̩����ŷ��ݺ����T��·컳�ɳ���������������������ͬ��ö�֪ͥ������������������ǧ��쾿��������Mݷ�ļ�ʥ�ӧ��˿�����������Ӯ��벷�ɼ�����刐������������������ë����С�پ���ҼԾ����˷������¡��Ф˴��Ұ�Ľ��١����Ʒ����ٳ�������س��������B���þ��Ů��ҥ����ܷ���ʱ���ܾ����ı֦����������ϧ�����������׻�����������޿Ψ����Ӫ���ᶰ����ȫ�����ɵ�D���ͼ��γ�����������Է������������ڵ����������������Ӵ�����ӥ��Ѥ���˵������Ǯп��쪸���ط�����������Ǭ������������䭳����ԣ��۪��ڡ����������������������_���Ω�������Ƚ��������Ὸ��ʟ@�|�˺�����ƺ���̾����Ŋu����������Ǫ������ӳ����������������ڛV���𥕄����ţǰ��������ü����ݦ��Ҳ�Л�������������������׽ۺ��ǳ���ݿ�ԫТ��Τ����ۭҫ٤���ܳ����չݶ������������Ԣ�����غ�ĭѸپ����Ũ��ް���ҿ�����۲��ں�����Ţ̫���������������θ��������ȹ�欿������D�F����������ú����ìH��˾������ϡ���������Ի���ɺ�������߰���ټ�������ǿ�����ұ������������Ѱ��ѡ�ԫ`δ����������٥殽�ѵ½�����޹¹��Ʈ������������ӬLΫ�ҹ�Ա�ܫ���������屣�ܵ�ө�Ĝ�����ݻٲͷ��Ӻ�������׺����߽���컱������ĮǾȨ�Ѵʩ������ۿũ���������˷������D������Ӿ��̶������߮���Ҧ쵸�����ʹ�¥�����۲���������������糸�Ѷ���������ʡ�׸��ǳ���������ٮͳԸ�ƻý�����������麸䵥𪼫��������������������渶�����ܬ���������ׯ�������ֲ����������ر�г�������������ת��������̺���������������ֿ������ů���������������Ͽ��������ο����������ί�����̷���̹�����ʦİ�����Fҹ�W�����庹��Ԭ�����Ƽ����ھ��ʻʰ���̨ۤϯ���ɱ��v�������ݸ�����ڱ�㰪�������������Ÿ�����ͭ���������ͻ��ٜR����������ϰ�����������س�������|��Ǳ���Ї���������������������ް�������¤ܭդ¼��⶷����ï�����������������ب��ؿ򭾫��鹻�����տ��ӡ�޷�ݯ����Ԧ����������ިԻ�j������������ұ����������۲�����ԯ������۳���ѿ����������ᩰ����ڵ�����������������Ǩ��³����������ղ������ʹ«���梼�Ƶ�S�黴��˨�����ɣ���������޲ξ������ĩ�����������ڼ������Х����Լ��׳������������ϩ��Ī����ӹ������Ӥ����������E�����½�ݰ��������ؼ��ȼ����޼�����ζ�����������ݥ�����߷���������������Ǽ��ν��֭�ɵУ����������������׾���꾱��̵�Ȱ������������������U��²ܷ����ϳܻ����ڵ������̷�ߵ������������������������������ݸ�������������ү����κ��ѭ���׼������������˼���븶��ˡ�������������ư�᣸���������ެ������ֵ�b�ѵi������ʣ��������Ӧ������������ڭ״����ޮ٣ظ�к���ּ���̰������䫸�TϾ��ǥ������Э���̵��ٵ���������Ͳ����¿��쭳����̾�ɪ�Ǹ���������奷�λ�Ե����ӹ��������¢Ѭ��������Ǻ����������Ļ��ي�������帳���ۺ�����ܵ��Ϭ�����̭��������ڿ��������ȼ�ģ����������������˿�������������;̴����������Ѻ�Ѯ榸չ�ÿٷ̸´Ǣ��Ϯ�ݶ���罼ڻ�����ĺ�c�����������鶯������μĻ䬶�«���������ռ�������ֿ���ڤ�˶��ֻ�����Ϥ�����Z墽��۽����ɷ���ǳ��l��ٶ�������Ļ����鼸�������������������������Ϲ������������ӽ��֤����ԡ����ٺ��������᮴����ߴ�Ƥ����������ش���ܼ��P���������֡ܦ��������ǽ����ҽͧף���ƿ��������������â���������ۺ�����Ч׻䱼öܿ�ݹ���彺���������������ޢΦƯ�ǹ�Ⱦ�|ئ���ܼ����͸�����ᨂ�nó������������׮��������خ�������Ե����Λh���������̬Qɫ��ǭ������������������ֱ�޸���ĺ�����������⾭�س佲�돀�����������ζ��Ŀ��侮��ǵ޳泪��ɴè뾻�ʿ�������ר��˵���������ݾ������ɳ�گ���ƨ�ҹ����������ҡѣ������������ϸ㢷�i�ɽ�̮���лͦ�Ž����D������鷶�������Ԯ�찂�������٩���۷���繧���������۫���ù�ƾ���Ҽ����������ƶ�����������޽���ʻ��෬ի���������������������������ۼ�����������ݮ�ɽ��������������Σѷ������������������������Ĳ�����ҷ�����Զ���������׼�������������������������媽�ʹ页�ֹ��ٯ���򴡱������������������k����îʶ���ʼ���������հ�е��������ޭ������������魬b�貣����Χ�������������Ѳ�����ͣ�����ӿ����֧鱺�������ԧ٭��������������ĵ���������������𾢾��Ƿ�������ɳ���̳��������������̲ں'

    m1='��������������訰��񰶰�����������İ˰װٰ۰ذ��������ᱪ�������������������ȱ̱���T���쮱������ϱ�������ٱ������������������������������������ƲŲĲƲɲβ���貲ٲݲ����乲���������ƫ`�����̳��˳���������衳�����������巳���鴬bة�ɳʳгϳǳ���̳γȳҳڳس۳ٳ������������������˴����������´ʴɴȴǴʹӴϴ����������槴������쵤����������������õµĵƵ���ҵ�ݶ�ѵص�馵ٵ�����������ඦ�����������������Ŷȶ˶ضܶ����䊊���������������������������[�����󷽷��ՕP���ŷ����Ƿ��������ܷ�����������︢��������٤���Ƹոڸٸ�۸�꽸��������������ب�����ٹ������������ȹع۹��ٹ��������������������Ϻ��ʺ������H�պ�嫺�����婺úº�껺ƜB𩰂�尺̺ϺκͺӺɺغպ׺��������޿����������ݦ�����������������������뻳������䡻�徻û����ƻ�諻������Իջ���������ݻ�ޥ����������٥���Ǽͼʼ��ü���𢼽���Ӽ��������μ׼����꯼�������������������������������������ݽڽܽ������޽�����Q��������誾�桽����ƽ��������ݼ����������������㽾������������������������žþ��ͽ��پپ�举����������������������������B������������������٩����������������ݿÿɿ�㡿�﬿����ӿ��������j�������������������������������������������������������������������������������������������������ٳ����۪������ݰ�����������������������������������������������������������������������������������R�������������������������������������¡¤¶³½¼��»·º���´�����������������������������۽������ܬ����ëï��öõü÷�������þ������������������������������������������������ؿ��ẕF������������������������ĩĭ��ĪĮīĬıĳľ������Ľ������������������������������Ţ��ţŮůŵ�Ÿ�����������������嫘���M������������Ʈ��Ƶ�Ʒ�ƽ��ƺƻ���������������������������������������ݽ���������������������ǧǪܷǨ�ǥǫ�ǰ���ǮǬǱǭٻ����ǿ��Ǿ��������������������������������������������������������ȫȨȪ����ȺȻȼȽ����������������������������������������F���������������ި������������������������ɣɭɽɼ��ɺ����������������ۿ��������|�������������ʤ��ʥ��ʢʦʫʩʮʯʱʵʿ���������������������������������ˡ����˧˫ˬˮ˳˴˸˷��˶��˼˹������ڡ����������������������̫̩̲̳��̷̶̴̹�������Ǐ|���������������������������������͡��ͤͥ͢������ͦ��ͧͨͬ١ͮͩͭͯ����ͫͳͷͼ;����������ݸ��������������������΢ΡΪΤΧ��ΨΩάΫΰγέί������δληξεοκ������������������������Ϧ��ϫ��ϣ����ۭ���ϧ��ϩ��ϡϪ�������������ϰ��ϲ����Ͽ�ϼ�������������������������������������������������������������������С����ТФЧУЦХг��л����о�����ݷп���нܰ��������������������������L����������ڼ����������������������������������ѡ�@����Ѥ�����ѧѩ��ѫ޹ѰѮ�����ѶѴѸѷѾ��������������۳������ܾ������������ٲ�����������������������������������������D�������������سҢ��Ҧ��ҥ��ҡң�����Ҫ��ҫҲұҰҵҶҷ������һ�������tҿҼ�������������������������������߮������������������߽�������������������������������������������נD޲��ܲ��������������������ӡطӦӢݺ��ӧӣ���ӥӭӯ��ӫӨөӪ�����������Ӯ��ӱӰӳӵӹӺܭ��ӽӾ��ӿ����������������ݯ������������������楫_����خ�������������������������ٶ������Ԧ������������������Ԣ��ԣ��������عԥԨԪ԰��ԫԭԲԬԮԵܫԴ��ԶԷ�Ը������hԿ������Ծ��Խ�����Ȋu�V�ܿ���������������������������������դհչստ�������������������������������������������������������������������������֤ں֣֡��ֱֲ֥֦֪֮����־��ۤ��ֿ�������������������������������������������ף��ׯ׳״׼׿پ�������������������������������������������'
    m21='������ļν���־�ƿ�С����һ����˼�����������������ΰ���ȶ������Ǳ��������ֳ���������ʫ��������ֳк���ҫ��������ѧ��������˰��ƿ����������ھ��Ҹ������չ�����������ʥ�ǽ�����������ܺ������ٻ���������������Ƹ�����άԪ������֮�ɱ��ŷ���׿�����п���ѩ������������ʿ����Զ���䴫�ʤ����Ѻ�ܻ���������˳��ǧ����ï巹�˺����ÿ�����չ�������ϸ߶��³������˽����ſ�����Դ�����Ӿ������ԣ���㱣������嫿ƼӺ����ŷ���ˮ����Т��̩����ɭ˹��ϲ����ʢ��ϣ���Ա����������������о�����沮��������ȫȪ��������������Ծ�س����ط��Ӣ�������ͩܰ������Ǿ��ī�޼��䱾ռ�����񾢳�ҵ�����Ŷ������캬ͥ�³������޺�֪�����������������뷢����͢�����ղ�ͬ������������������������Ӧ�������������ϻ۷�������������˫ع˧�̱���Ӷ�Ȩ������������˴�Ǭ���������ƽة����������ӽ�������ܴ���·�������Τ�һݾ÷���ľ�������ֿ���ͯ��̫ܲ������������ʺ����۷�ӳ��ӭ���˸Ϊ��������������Хܷ�����Ⱥٳ����������������Ԩ��Ϧ����ϴ���ɽЦ����ͮΨ��Ĭ��������ٵ�F�����������Ź�¡�������������ݾ�������������Ը��Ӱ��׾��ںó��մ滯������Խ��Ǳ���ʯ�������ؼ�˶�沨�ʵt������ʱ����½�ز�ݷ������»��������Ң����������ʩ��������ޥս�Ⱥ���κ��ǿʦ����������ʮ�����ӯ��߮��ӿƷ���ٶ��̳��η����ڵ����ټᱱ�ۿ��׳��������������鈐�������h����Ωտ�B������ԭۤ�������衽�Ч�ص������ӡ��������ϧԥ��ѫ���첽�����޹���ͤ��ǰ��ϫ��᷺��׸�������γ֣�Ѵ������������˱�����װ����ŵ���Ľ����ֲ��ǫ��������ʹ˹��Ʊ�ӱ�������³������Ҷ���������̸����ز��̻�������������������Ρξ�Ҽ֦���̾�پ˿����нͨ����У����ټ��ϰ��ϸׯ�건�㹫���@�����ػ������������ٲ�������Ӻ�ݴ��ʏ���ε���������ұ��F¶����Ī�ؿװ��ȕ�������ĭ����𥻴����ѡ���������������ӱ������ﲻ�㳱˾��٤�����о�����Կ������������������ҿ����ݸ������ӣף��幽��ȼ��������δ�о����ƶ�خ�������Ѿ�������ݯ��������赹�֥��������õ����ë������Ѹ�������ӵ������������Ԣ˷����������������ݽ����԰������������Ӯ�����������Bܿ��ٶ����ݺ�����������ŵ������Ѿ���ܶ���������M��䰪������ϻ�����ư�����������ȹ��������Ǯ��ͦ��Ƚ���Ӿ�������仾����Ƽ���Ϫ�����ų���ϯ����ݼ�����ֻ�����έ������������������������۾�Ԭ��������������ԷҪ��ϡ�����������ڡ����������Ҷ�����̹п����Ԧ�ɺ����������������ʶ��´������޲����嶻üϼ���������Ȼ���ö�����������ø�Ů���縴��üҦ��ԫ��¥������������謌k������٥��������º��������Ϋ�Lӧλ��������ѵ���������Ҳ۪����١������������ӨƮ�������������ẵ��������̿�����Ե��豟j����þ��������������������ڼФ����ͳ���������ݹ����ִ�ʺ�ϩ���������������اŢ��������������������������Э��ᶸ����|����Һ���������ղ����«����������������Ҵ����������񼰽�����صv�ظ����D��ĺ٩������������嵭ۭ������载���������ٻ�ȳ��������Ѥ���Ʒ��ů����ֿ���������������������������_��ɼͭ�b���˴�������Ӫ����Ұ¼��������ۼ�������������T���¬�������������˵�͡���ײ��������������˨�����ָ��������ܫ�������亹�위������ڱ����������𰡜��������ƺ��ɵ����՟������ܼ쳵���վ����ɛVμ�������ұ��ܬH������̲θ��������¾����창���������˰������������������ᱤ�л�����ɺϵ������ƃ����ʵ߽���������媏�ֹ�����ʰ�����E��Ի������Ǫ���������޿�S̴�˿����б�������դ������������Բ��������������Ԥ���������籺�����ӹͫԼ��޼Ǩ�������ּ���ި���ſ������Ÿ۴�֤�����񺾣��ĵ̸�������گ��������ĩ���������������譵Ѿ������߷������Ȱ�ļ�����ѷ�ıں�������ԡͼݰ���̵�ȼ���ȱ���������ũ������������Ѱ�����ҹ��꾶��������������չ���Ǿ��޹����ۥ�����ٺ��䢋C�������������ܲ����޹�ǥ�廹��ؿĻӫ��ӥ������UϢٲ�������֡����ʾ��Ϯ����ҳ��Ը����Į������ˬѦӤţ�ͷ���������л���ⵥ���Ϥ��Ǳʽ����ȵ���������ǳ����Ѵ�������Ԯ���������������������΢�R���ҽʷ����ױ����֧ܬ�����ب������u��������ɣ��٧�����뵳�Ǹ�����۳ί����������������������İ�������Ǣ�������������ֱʡ�ɳ���������赽�ｮݽܾ����ѭ�����ۻ����������������������������ģĳ����̷��ԯΦ������꼳����ݦ����ֻ���ʲ����㹲������������鷺ˡ�ٱ��������¿Ŀ��������ƨ˲�޿���𮵶������հ������������ȡ�m��׼�Ƶ����˵���Ų̃����ڤο�����Ա��ئ��آ�����Ӱ������Ӱ�ںڹ�����³ƹ�������ذ���������ֻ������������������ך��������ݬ��������B��������ެ������ı��̸������������������ٮ��á޽��䱵�¢������ݥ�����ϛh����������������Ǽ��ٽ�޸����������ᵺ�ҷ����¤�����纾�ڷ�����饿�îͷ̦��¹�ڼ�������ݶ���η��ӊ���϶ȱ������ȿ��������ύ�����֬��ŷ������Q�μ�Ư�i�߽���������÷ڵ�ҹ���������������ԅ�������籸��q��챫Ÿ�����������������Ѿϳ����׳ִ������º�ר���ص����������Բ̾��أ������������ٱ|®���������Ӵι���ɴ�̵���ٺ���趽�����������ŵ������ء���Ǽ�Ƶ��������Ѯ����ʼ���̰ݼ������۹�����˩�����߷���Ĳ�P�����Ǜ�ݾ����ݿȸг���ŵ�ĵ����������ܸ�ݻѿ������������޸����������﷩����񷻵�����O���Ĵ������ͷ��ǻ�ǭ�������������ӵ�ѣ��Ѷ����ֵ��������������������������������������˽��Ƹ̶۫�����غ����װ�����ҹ尻��٫ﯷ���Ⱦ���������������������뿼�WҬ��׾������ڭ����Ժ������������޽�����ת�����ȳ��ө�����붷���ѿ�'
    m22='�ν���������Ķ�����ƽ���������η�����ΰ��ȻԴ��������ǿ���ͮ��������ͩ���������򲨳�����ܱ���Զ�����������鰲ɭ껿�����������Ӣ��𩳿��������俱������ɹ⽭־��Ȩ��һԪ�㺣�����淲�ǿ����·�����ɽ���ʺ����������������ʤ����֮�촺�������Ǻ쿥���������̱����������ҫͯ����ȫϣ���帻��Ȫ�ı����������úʹ����������೼�ϲ�Ң˳��Ⱥ�غ������������ī�����Ծ�����ˮ˶�����ѫ����ʢ����������ջ��ǫ����ͺ�������¡��������ϲ��ѧ����ة�ӱ��������Ž��ڽ�����ά�������Ԩͬ������̩����ҵ��͢�ɷ�����������ǽ������ڱ��������ͥ�������尿ɲӸ������˺ø����˼�����ر��Ƚ��׿�����ý���Խ��������ԣ��Ϊ��ͨ������������������������ѩ������ԭ��о�������������ʥ������˼��˧�ڳ������ݻ��������Ծ�Ӽ�۷ǰ��񴿺�ܰ�������俪��Ǭ���������ʯ������׸�ϫ��ïʫ�񳾺��Ų����賩����������������Ĭ�������֦ع�����޶�����γľŵ����짳���ܲ�����ط���������ӱ�������ź�������������������ฦ�����չ�����������ȼ��»����˴���ǳ���ӡ��������������������˸����׳�ѹ�������������������������ͫ����B�ɳ���������������������·�ֳ�������������ӯ���˺�������������贳������˫��̫����Ե�������ԥ�ò��鱱���н������������֥����Ѹ���������ٴ���������Ϧ������������ӥ������������屾�ȶ���񴵤Կ�tͤ�����ɼ����������������Ө���ռӫh��Ӫ���Ρ�鷼����ε��Ұ�Ӹ��������Ĵ�������͕F����Ѿ����������Тޥ��ΤέϪ��Ӿ��ܷ��˹��@�շ�º��ǧ�������˺�����Х�������������ʮ��������ݽ������Ҷ�T��������֪��д�ط����ң��ǰ�ᾩ�װ����˽�԰�廯�ԏ������񽾾���õ�����������������������䲲���������ٳʵ�١��ëܿ�����������÷��ö¶���ʱ������������������ӧ���ܵ���������ӭ����������ũ������˷����Ҽ�갬Цҥ�ͳ�������ӿ�Bݷ�����̷�����۰�ֲ��Ӯ��ׯ��ʿı����ϧ��ξ���ӳ��ؽ�����п������ݼ�����д��Ů�ɲ�����������Ψ���Ͼ�¼������豼���Ǯ����С��ɺ����ͼ��ʦ������������������콳�������Ѥ����ݿ����޿�����������׾��ߟj����������������������͡����Ӧ�|�������������۪��ͦ�������ڡ�Ƴ�����������þ��ͭ���ʫ_���������ж��̰�ü����������������������ƺ���������椕D���Ӱ��籴���ĭս泛V����Ӻ٤����Ω�������D˿���M��Ũ�ܷ�ӫ�������������ط���������ԫ�������������������H�������ҿ��ί���񕄭[���Ź������ﲳ��������ݦ��ϡ���ڸ�����貹�������ӽ����ݺӣ³��޹���Ȋu��¥Ţ���������λ���ڵ��پ�����������ԸԢ̶����������������ٵ���ۭ������Է����өѷ���������Ӽ�ţѵ����ףϰ������Ʒ���������خ��߽ƻ��ŸƮ�ܲ���ͳУ�鹷���ӳ�霏��ټ���е�����ٲ����½���ҫ`���Ѵ�ּ����Ϋ��ʩ�����羸�ẰĹŹ�������û�������߮��ݻģ����ۿ������覺����������������٥��������������Ѱ��ͷٻ������κ�������Բ������������ϯδܫ���Ҿ����ˬ�ε����������ƿ�����������������Ѷ������٩���������������տĮұ����乲�ϼԱ麼��Ȳ����ܾ��ѡ�ָ��̱���ب��������L�����D�՜R�����н��ۤҦ���Ƚ��緯�ԑ�����૸�������v�����ڿ�����������������������΋S����Ի�W����Ǩ��������իӹ��Ǳ��桽�����ڼ�������۱�����г�������������̹ĩ�������������º�ϿǪި̴������ֿԯܬ����������±���ҹ��Ǿ������������ռ������¤�ý���Ԭ���θ�����������޲�ַ��F����ؿ�����ڱ�|�Ȱ������뫘΢��������������Ͻ���ѿ��������Ԧ�����������ݺ�ʹ����粴ɣ��ܭ�������ᩲԿ���ڻ���ᷲ�������ο������ܺ�������̨ŷ��������դ����䵵��������ʽ�������������̽����ؾ۾��������𲻼������������س����������Ľ����İݯ���ڼ�����Ӥ�������۳������з⼾�����ϩ�����˨�����������ʶݶ�����ΰ�𢶱Ƶ���׸����������Ч���������ڸ�����ů��Լ���������Ī���޲�妴���׮�Ź�饰������ǥ�������ԡ��������������Ϲ�ǢΦٷ�ù��۷������٣佲��������Ⱦ�����¹��򥴡�ڵ���չ���������������������������Ф����ּ����������۫�����ȷ�ڵ������ü����Ŀ��ﭷ�����Ϥ��ɴ���������������֧��䱱�������������������l���������ү��������������ǭ����ڭ�������񰂶�;���ӷ����̴����޸�����䫿�޼����Ѯ�óÿ��ۺ�����ٶ�����è��������������������������μ���緺ͧ�����ú���渻�������ݮ������ئެ�������ɜU��ܦΣ����ת�n��᡽����غ�������ɵ���־�ν�۲ο����ڽ�����������������֭����������������״��������ֹ��޽����̸������Ⱦ�����ٸ�ɪҡ��ѣ��������Ҫ奱���Թ໩���ñ���â���۳���������Ѭ������Ȼ��������������̮�����¿��ޢ��������������̻�Ԯ�������Э��������ٺ�����ù˳�̷����׼���쵺Ƥ�����������Թ��ɷ���Ĳ����ݸ������Ҳ����հ�����������¿�bٮ����Ϯ��������۲���������������ƨ�۰�˵̳�Ļ��������������������ݾ�۶�ོ��̲����ڤ������Z糾�ٯ��뾱|��������������ֵ��۽ϸ��ӵ�ӏ����Ủ���¹�Ϭ���������̭����������޸���ɻ��T������嶱�����˾ޮ��ظ�ǼϷ������׷����ޭ��ᮺ�����ĵ����鷴��ܕP����������������ʹ�����������ߌk��ԧ������ۼ�������̳«���ֺ���˵�Ӻ���ר�������׹�ʣ������ϳ��������������ܻ������������Ǽ�������˷�֤���h������״��𶣹�������ֱ��ĵ�ҷ�����ʡ�ٹ��ƾ����⹲���ռ���Ѳ�������ݹ������������������������������������˳�گ��׼�������֡�����cζĺ���������Ư�ĵi���ق缸�D��֣�������ݷ�������ܬQ�����ӿ������������������������������Χ��壅�������������޺���������¢������䬵�ں����׻ҽ��ѭ���ʾ�����ǳ�ͽ��������������������������Ͼ�������Ҷ����������i�ܼ��ͣ�î�ٳ�������ҿ�������鴳뼨��ݥ����٭����´�������������ɫ����ݰ���ʶ����䲼��E�͵�ˡ���������Ȱƿ�����Ｖ�������姰���������굥������'
    xing=xingnote[np.random.randint(0,len(xingnote))]
    xingbie=np.random.randint(0,2)
    zichang=np.random.randint(0,2)
    if xingbie==0 and zichang==0:
        ming=f1[np.random.randint(0,len(f1))]
    if xingbie==1 and zichang==0:
        ming=m1[np.random.randint(0,len(m1))]
    if xingbie==0 and zichang==1:
        ming=f21[np.random.randint(0,len(f21))]+f22[np.random.randint(0,len(f22))]
    if xingbie==1 and zichang==1:
        ming=m21[np.random.randint(0,len(m21))]+m22[np.random.randint(0,len(m22))]


    return xing,ming


count=0
# xingmingceping('��','����')
data=pd.read_excel(r'class_name.xlsx').����.tolist()
for i in range(74):
    # xing,ming=getname()
    xing='��'
    ming='��'
    print (xing,ming)
    result=xingmingceping(xing,ming)
    if result:

        sancai,jixiong,mingge,elseword=result
        print (sancai,'\n',jixiong,'\n',mingge)
        for word in elseword:
            print (word,end='\n')
    else:
        count+=1
        print ('��δƥ��')

    print('����' + str(i + 1) + '��', '�쳣' + str(count) + '��')
    time.sleep(10)
